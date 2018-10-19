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

@pytest.fixture()
def sales_data():
    data = {
        "attendant_name": "anyatibrian",
        "product": "tourch",
        "quantity": "9000",
        "unit_price": "400"
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


# checking whether the list is not empty
def test_get_products_endpoints(client):
    response = client.get('api/v1/products')
    assert len(response.data) >= 0


# testing the post product endpoint


def test_get_single_product_endpoint(client):
    """testing testing get single product endpoint"""
    response = client.get('api/v1/products/{}'.format(1))
    assert response.status_code == 200


def test_get_product_id_not_exist(client):
    """testing whether the product id exist """
    response = client.get('api/v1/products/{}'.format(1))
    assert b"product does not exist" in response.data


def test_post_sales_endpoint(client, sales_data):
    """ testing the post sales endpoints"""
    response = client.post('/api/v1/sales', data=json.dumps(sales_data))
    assert response.status_code == 201


# testing the post product endpoint
def test_get_single_records_endpoint(client):
    """testing the get single records endpoints"""
    response = client.get('api/v1/sales/{}'.format(1))
    assert response.status_code == 200


def test_get_record_id_not_exist(client):
    """testing whether the record  id exist """
    response = client.get('api/v1/sales/{}'.format(1000))
    assert b"such a record does not exit" in response.data


# testing the post product endpoint
def test_get_all_sales_records_endpoints(client):
    """testing the post product endpoints"""
    response = client.get('api/v1/sales')
    assert response.status_code == 200

