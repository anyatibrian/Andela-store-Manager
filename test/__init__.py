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
        "attendant": "anyatibrian",
        "product": "tourch",
        "quantity": "9000",
        "unit_price": "400"
    }
    return data
