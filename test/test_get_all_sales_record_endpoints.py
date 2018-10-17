from test import client, data
from flask import json


# testing the post product endpoint
def test_get_all_sales_records_endpoints(client):
    """testing the post product endpoints"""
    response = client.get('api/v1/sales')
    assert response.status_code == 200
