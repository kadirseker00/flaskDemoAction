import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}

def test_add(client):
    response = client.get('/add/1/2')
    assert response.status_code == 200
    assert response.get_json() == {"result": 3}

