from test import client, data
from flask import json


# testing the post product endpoint
def test_get_single_records_endpoint(client):
    """testing the get single records endpoints"""
    response = client.get('api/v1/sales/{}'.format(1))
    assert response.status_code == 200
