from flask import json, request
from Api.modules.product_modules import Products
from ..apiv1 import api_blueprint
from Api.helpers_functions import empty_fields


@api_blueprint.route('/products', methods=['POST'])
def post_products():
    json_data = request.get_json(force=True)
    if empty_fields(json_data['product_name'], json_data['description'], json_data['quantity'], json_data['price']):
        return json.dumps({'message': 'some fields are empty'}), 200
    product = Products()
    product.create_product(product_name=json_data['product_name'],
                           description=json_data['description'],
                           quantity=json_data['quantity'], price=json_data['price'])
    return json.dumps({'message': 'product created successfully'}), 201
