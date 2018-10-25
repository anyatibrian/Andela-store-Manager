from Api.modules.products import product_list
from flask import jsonify, make_response
from ..apiv1 import api_blueprint


@api_blueprint.route('/products/<int:product_id>', methods=['GET'])
def get_single_product(product_id):
    """endpoint for getting a single products into the product list"""
    if 0 < product_id < len(product_list):
        products = [products for products in product_list if products['id'] == product_id]
        return make_response(jsonify({'products': products[0]}), 200)
    else:
        return make_response(jsonify({'message': "product does not exist  "}), 200)