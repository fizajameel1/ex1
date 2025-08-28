from app import app

def test_homepage():
    with app.test_client() as client:
        resp = client.get('/')
        assert resp.status_code == 200

def test_about_page():
    with app.test_client() as client:
        resp = client.get('/about')
        assert resp.status_code == 200
