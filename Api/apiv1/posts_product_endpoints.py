from Api.modules.products import Products
from flask import jsonify, request, make_response
from ..apiv1 import api_blueprint


@api_blueprint.route('/products', methods=['POST'])
def post_products():
    """endpoint for post products into the product list"""
    json_data = request.get_json(force=True)
    product = Products()
    product.create_product(json_data['product_name'], json_data['description'],
                           json_data['quantity'], json_data['price'])
    return make_response(jsonify({'message': "product created successfully "}), 201)

