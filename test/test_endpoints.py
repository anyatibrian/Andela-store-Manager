from Api import create_app
import pytest
import json


@pytest.fixture(scope='module')
def client():
    """fixture for initializing our test client """
    app = create_app('testing')
    test_client = app.test_client()
    return test_client


@pytest.fixture()
def data():
    """fixture for creating the test data"""
    data = {
        "product_name": "camera",
        "description": "the is ultimate",
        "quantity": 9,
        "price": 900000
    }
    return data


def test_post_product_endpoint(client, data):
    """testing for post product endpoint"""
    response = client.post('/api/v1/products', data=json.dumps(data))
    assert response.status_code == 201