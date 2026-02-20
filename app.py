from flask import Flask, render_template, request, redirect, session, url_for
from flask_babel import Babel
from models import db, Store, Product, Shelf, InventoryItem

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_secreto_super_seguro'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BABEL_DEFAULT_LOCALE'] = 'es'

# Inicializar DB y Babel
db.init_app(app)

def get_locale():
    # Retorna el idioma activo en la sesión del usuario (o español por defecto)
    return session.get('lang', 'es')

babel = Babel(app, locale_selector=get_locale)

# ==== Context Processor ====
@app.context_processor
def inject_conf_var():
    return dict(CURRENT_LANGUAGE=session.get('lang', 'es'))

# ==== Rutas ====
@app.route('/set_lang/<lang>')
def set_lang(lang):
    if lang in ['es', 'en']:
        session['lang'] = lang
    return redirect(request.referrer or url_for('dashboard'))

@app.route('/')
def dashboard():
    total_stores = Store.query.count()
    total_products = Product.query.count()
    
    # Calcular stock total de toda la cadena (suma de qty_total o sumando qty)
    items = InventoryItem.query.all()
    total_stock = sum(item.qty for item in items)

    return render_template('dashboard.html', 
                           total_stores=total_stores, 
                           total_products=total_products, 
                           total_stock=total_stock)

@app.route('/stores')
def stores_index():
    stores = Store.query.all()
    return render_template('stores_index.html', stores=stores)

@app.route('/stores/<int:store_id>')
def store_detail(store_id):
    store = Store.query.get_or_404(store_id)
    # Todos los items de inventario de esta tienda, con info de producto y balda
    inventory = InventoryItem.query.filter_by(refStore=store_id).all()
    return render_template('store_detail.html', store=store, inventory=inventory)

@app.route('/products')
def products_index():
    products = Product.query.all()
    return render_template('products_index.html', products=products)

@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    # Ubicaciones donde está disponible este producto (tienda y balda)
    inventory = InventoryItem.query.filter_by(refProduct=product_id).all()
    return render_template('product_detail.html', product=product, inventory=inventory)

@app.route('/stores/new', methods=['GET', 'POST'])
def store_new():
    if request.method == 'POST':
        store = Store(
            name=request.form['name'],
            image=request.form['image'],
            address=request.form['address'],
            location=request.form['location']
        )
        db.session.add(store)
        db.session.commit()
        return redirect(url_for('stores_index'))
    return render_template('store_form.html', store=None)

@app.route('/stores/<int:store_id>/edit', methods=['GET', 'POST'])
def store_edit(store_id):
    store = Store.query.get_or_404(store_id)
    if request.method == 'POST':
        store.name = request.form['name']
        store.image = request.form['image']
        store.address = request.form['address']
        store.location = request.form['location']
        db.session.commit()
        return redirect(url_for('store_detail', store_id=store.id))
    return render_template('store_form.html', store=store)

@app.route('/stores/<int:store_id>/delete', methods=['POST'])
def store_delete(store_id):
    store = Store.query.get_or_404(store_id)
    db.session.delete(store)
    db.session.commit()
    return redirect(url_for('stores_index'))

@app.route('/products/new', methods=['GET', 'POST'])
def product_new():
    if request.method == 'POST':
        product = Product(
            name=request.form['name'],
            image=request.form['image'],
            size=request.form['size'],
            price=float(request.form['price'])
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('products_index'))
    return render_template('product_form.html', product=None)

@app.route('/products/<int:product_id>/edit', methods=['GET', 'POST'])
def product_edit(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.image = request.form['image']
        product.size = request.form['size']
        product.price = float(request.form['price'])
        db.session.commit()
        return redirect(url_for('product_detail', product_id=product.id))
    return render_template('product_form.html', product=product)

@app.route('/products/<int:product_id>/delete', methods=['POST'])
def product_delete(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('products_index'))

if __name__ == '__main__':
    with app.app_context():
        # Crear base de datos en caso de no existir, cuidado si ya está creada.
        db.create_all()
    app.run(debug=True, port=5000)
