import pytest
from app import app
from models import db, Store, Product

@pytest.fixture
def client():
    # Configurar la app para testing (base de datos en memoria para no ensuciar la real)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            
            # Crear datos mínimos para pruebas de rutas
            store = Store(name="Test Store", address="123 Test St", location="{}")
            product = Product(name="Test Product", price=9.99, size="1x")
            db.session.add(store)
            db.session.add(product)
            db.session.commit()
            
            yield client
            
            # Limpiar tras las pruebas
            db.session.remove()
            db.drop_all()
