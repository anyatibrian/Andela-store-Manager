from test import client, data
from flask import json


# testing the post product endpoint
def test_get_product_endpoints(client, data):
    """checking wether some data was posted"""
    response = client.post('api/v1/products', data=json.dumps(data))
    assert response.status_code == 201
    """getting all the products that were posted"""
    response = client.get('api/v1/products')
    assert response.status_code == 200
