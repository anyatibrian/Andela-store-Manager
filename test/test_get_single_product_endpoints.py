from test import client, data
from flask import json


# testing the post product endpoint
def test_get_single_product_endpoint(client):
    """testing testing get single product endpoint"""
    response = client.get('api/v1/products/{}'.format(1))
    assert response.status_code == 200
