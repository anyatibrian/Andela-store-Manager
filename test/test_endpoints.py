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


def test_checking_for_empty_field(client):
    response = client.post('api/v1/products', data=json.dumps({
        "product_name": "",
        "description": "",
        "quantity": "900",
        "price": "2000"
    }
    ))
    assert b"some fields are empty" in response.data


def test_post_data_type(client):
    response = client.post('api/v1/products', data=json.dumps({
        "product_name": "touch",
        "description": "people like it",
        "quantity": "popo",
        "price": "popolipop"
    }
    ))
    assert b"invalid types" in response.data


# testing the post product endpoint
def test_post_product_endpoints(client, data):
    """testing the post product endpoints"""
    response = client.post('api/v1/products', data=json.dumps(data))
    assert response.status_code == 200
