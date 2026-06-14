import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['app'] == 'iCargo Tracker API'
    assert data['status'] == 'ok'


def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'healthy'


def test_get_all_shipments(client):
    response = client.get('/shipments')
    assert response.status_code == 200
    data = response.get_json()
    assert 'shipments' in data
    assert len(data['shipments']) == 3


def test_get_shipment_by_awb(client):
    response = client.get('/shipments/CG001')
    assert response.status_code == 200
    data = response.get_json()
    assert data['awb'] == 'CG001'
    assert data['origin'] == 'Chennai'


def test_get_shipment_not_found(client):
    response = client.get('/shipments/INVALID')
    assert response.status_code == 404


def test_get_by_status(client):
    response = client.get('/shipments/status/delivered')
    assert response.status_code == 200
    data = response.get_json()
    assert 'CG002' in data['shipments']
