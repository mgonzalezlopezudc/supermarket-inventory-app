import random
from app import app
from models import db, Store, Product, Shelf, InventoryItem

def generate_test_data():
    with app.app_context():
        # Limpiar BD existente
        db.drop_all()
        db.create_all()

        print("Generando tiendas...")
        stores = []
        for i in range(1, 5):
            store = Store(
                name=f"Supermarket Store {i}",
                image=f"https://images.unsplash.com/photo-1578916171728-46686eac8d58?w=800&q=80",
                address=f"Avenida Principal {i*10}, Ciudad Central",
                location='{"type":"Point","coordinates":[-3.703790, 40.416775]}'
            )
            db.session.add(store)
            stores.append(store)
        db.session.commit()

        print("Generando baldas por tienda...")
        shelves = []
        for store in stores:
            for i in range(1, 5):
                shelf = Shelf(
                    name=f"Shelf {i} (Store {store.id})",
                    capacity=100,
                    refStore=store.id
                )
                db.session.add(shelf)
                shelves.append(shelf)
        db.session.commit()

        print("Generando catálogo de productos...")
        products = []
        product_names = ["Manzanas", "Leche Entera", "Pan de Molde", "Huevos Docena", 
                         "Aceite de Oliva", "Zumo de Naranja", "Café Molido", 
                         "Galletas de Chocolate", "Atún en lata", "Arroz Blanco"]
        images = [
            "https://images.unsplash.com/photo-1619546813926-a78fa6372cd2?w=500&q=80", # manzanas
            "https://images.unsplash.com/photo-1550583724-b2692b85b150?w=500&q=80", # leche
            "https://images.unsplash.com/photo-1598373182133-52452f7691ef?w=500&q=80", # pan
            "https://images.unsplash.com/photo-1498837167922-ddd27525d352?w=500&q=80", # huevos
            "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=500&q=80", # aceite
            "https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?w=500&q=80", # zumo
            "https://images.unsplash.com/photo-1559525839-b184a4d698c7?w=500&q=80", # cafe
            "https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=500&q=80", # galletas
            "https://images.unsplash.com/photo-1558222218-b7b54eede3f3?w=500&q=80", # atun
            "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=500&q=80"  # arroz
        ]

        for i in range(10):
            product = Product(
                name=product_names[i],
                image=images[i],
                size="1 Kg/L",
                price=random.uniform(1.5, 9.99)
            )
            db.session.add(product)
            products.append(product)
        db.session.commit()

        print("Asignando al menos 2 productos a cada balda...")
        for shelf in shelves:
            # Seleccionar 2 productos al azar para esta balda
            sampled_products = random.sample(products, 2)
            for prod in sampled_products:
                qty_in_shelf = random.randint(10, 50)
                item = InventoryItem(
                    refProduct=prod.id,
                    refStore=shelf.refStore,
                    refShelf=shelf.id,
                    qty=qty_in_shelf,
                    qty_total=qty_in_shelf * 2 # Simulación de total en tienda
                )
                db.session.add(item)
        
        db.session.commit()
        print("Datos autogenerados correctamente.")

if __name__ == '__main__':
    generate_test_data()
