import pytest
from models import db, Store, Shelf, Product, InventoryItem

def test_store_creation(client):
    store = Store(name="Local 1", address="Calle A")
    db.session.add(store)
    db.session.commit()
    
    assert store.id is not None
    assert store.name == "Local 1"

def test_shelf_creation(client):
    store = Store.query.first()
    assert store is not None
    
    shelf = Shelf(name="A1", capacity=50, refStore=store.id)
    db.session.add(shelf)
    db.session.commit()
    
    assert shelf.id is not None
    assert shelf.refStore == store.id
    assert shelf.store.name == store.name

def test_inventory_item_creation(client):
    store = Store.query.first()
    product = Product.query.first()
    
    shelf = Shelf(name="B1", capacity=20, refStore=store.id)
    db.session.add(shelf)
    db.session.commit()
    
    item = InventoryItem(refProduct=product.id, refStore=store.id, refShelf=shelf.id, qty=10, qty_total=10)
    db.session.add(item)
    db.session.commit()
    
    assert item.id is not None
    assert item.qty == 10
    assert item.product_ref.name == product.name

def test_store_cascade_delete(client):
    store = Store(name="A borrar")
    db.session.add(store)
    db.session.commit()
    store_id = store.id
    
    shelf = Shelf(name="A1", refStore=store_id)
    db.session.add(shelf)
    db.session.commit()
    
    # Comprobar que existen
    assert Shelf.query.filter_by(refStore=store_id).count() == 1
    
    # Borrar la tienda
    db.session.delete(store)
    db.session.commit()
    
    # Comprobar borrado en cascada
    assert Shelf.query.filter_by(refStore=store_id).count() == 0
