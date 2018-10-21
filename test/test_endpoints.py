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


def test_check_empty_product_list(client):
    response = client.get('api/v1/products')
    assert b"you don't have any product yet" in response.data


# testing the post product endpoint
def test_post_product_endpoints(client, data):
    """testing the post product endpoints"""
    response = client.post('api/v1/products', data=json.dumps(data))
    assert response.status_code == 201


# testing the post product endpoint
def test_get_product_endpoints(client):
    """getting all the products that were posted"""
    response = client.get('api/v1/products')
    assert json.loads(response.data)['products'][0]['product_name'] == "touch"
    assert len(json.loads(response.data)) == 1
    assert response.status_code == 200

