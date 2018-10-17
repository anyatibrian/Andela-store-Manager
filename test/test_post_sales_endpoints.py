import json

from test import client, sales_data


def test_post_sales_endpoint(client, sales_data):
    """ testing the post sales endpoints"""
    response = client.post('/api/v1/sales', data=json.dumps(sales_data))
    assert response.status_code == 201
