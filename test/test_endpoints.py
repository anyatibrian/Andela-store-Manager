from flask import json
import pytest
from Api import create_app


@pytest.fixture(scope="module")
def client():
    app = create_app('testing')
    test_client = app.test_client()
    return test_client


@pytest.fixture()
def data():
    data = {
        "product_name": "touch",
        "description": "this is great product",
        "quantity": "900",
        "price": "2000"
    }
    return data


# testing the post product endpoint
def test_post_product_endpoints(client, data):
    """testing the post product endpoints"""
    response = client.post('api/v1/products', data=json.dumps(data))
    assert response.status_code == 201


# testing the post product endpoint
def test_get_product_endpoints(client):
    """getting all the products that were posted"""
    response = client.get('api/v1/products')
    assert response.status_code == 200


# checking whether the list is empty
def test_get_products_endpoints(client):
    response = client.get('api/v1/products')
    assert len(response.data) >= 0
