import json

from test import client


def test_post_sales_endpoint(client):
    response = client.post('/api/v1/sales', data=json.dumps({
        "attendant_name": "anyatibrian",
        "product": "tourch",
        "quantity": "9000",
        "unit_price": "400"
    }))
    assert response.status_code == 201
