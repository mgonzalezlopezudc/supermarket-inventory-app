from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255))
    address = db.Column(db.String(200))
    location = db.Column(db.Text)  # JSON string para GeoJSON

    shelves = db.relationship('Shelf', backref='store', lazy=True, cascade="all, delete-orphan")
    inventory_items = db.relationship('InventoryItem', backref='store_ref', lazy=True, cascade="all, delete-orphan")

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255))
    size = db.Column(db.String(50))
    price = db.Column(db.Float)

    inventory_items = db.relationship('InventoryItem', backref='product_ref', lazy=True, cascade="all, delete-orphan")

class Shelf(db.Model):
    __tablename__ = 'shelves'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Integer)
    refStore = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)

    inventory_items = db.relationship('InventoryItem', backref='shelf_ref', lazy=True, cascade="all, delete-orphan")

class InventoryItem(db.Model):
    __tablename__ = 'inventory_items'
    id = db.Column(db.Integer, primary_key=True)
    refProduct = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    refStore = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
    refShelf = db.Column(db.Integer, db.ForeignKey('shelves.id'), nullable=False)
    qty = db.Column(db.Integer, default=0)
    qty_total = db.Column(db.Integer, default=0)
