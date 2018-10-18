from Api.modules.products import product_list
from flask import jsonify, make_response
from ..apiv1 import api_blueprint


@api_blueprint.route('/products', methods=['GET'])
def post_products():
    """endpoints to fetch all the products"""
    if len(product_list) != 0:
        return make_response(jsonify({'products': product_list}), 200)
    else:
        return make_response(jsonify({'message': "you don't have any product yet "}), 200)


