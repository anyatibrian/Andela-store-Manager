from test import client, data
from flask import json


# testing the post product endpoint
def test_post_product_endpoints(client, data):
    """testing the post product endpoints"""
    response = client.post('api/v1/products', data=json.dumps(data))
    assert response.status_code == 201
