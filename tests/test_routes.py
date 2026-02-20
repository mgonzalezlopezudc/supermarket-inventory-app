def test_dashboard_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"InventoryPro" in response.data

def test_stores_route(client):
    response = client.get('/stores')
    assert response.status_code == 200
    assert b"Test Store" in response.data

def test_store_detail_route(client):
    # La tienda 1 existe por el fixture
    response = client.get('/stores/1')
    assert response.status_code == 200
    assert b"Test Store" in response.data

def test_store_detail_not_found(client):
    response = client.get('/stores/999')
    assert response.status_code == 404

def test_products_route(client):
    response = client.get('/products')
    assert response.status_code == 200
    assert b"Test Product" in response.data

def test_product_detail_route(client):
    response = client.get('/products/1')
    assert response.status_code == 200
    assert b"Test Product" in response.data

def test_language_switch_route(client):
    response = client.get('/set_lang/en')
    # Debe hacer un redirect (código 302)
    assert response.status_code == 302
