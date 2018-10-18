from test import client, data
from flask import json


# testing the post product endpoint
def test_get_product_endpoints(client):
    """getting all the products that were posted"""
    response = client.get('api/v1/products')
    assert response.status_code == 200


# checking whether the list is empty
def test_get_products_endpoints(client):
    response = client.get('api/v1/products')
    assert b"you don't have any product yet" in response.data
