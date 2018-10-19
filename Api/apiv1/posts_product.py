from Api.modules.products import Products
from flask import jsonify, request, make_response
from ..apiv1 import api_blueprint
from Api.utilities import checK_empty_field, check_types, check_remove_white_spaces


@api_blueprint.route('/products', methods=['POST'])
def post_products():
    """endpoint for post products into the product list"""
    json_data = request.get_json(force=True)
    product = Products()
    # checking whether the fields are empty
    if checK_empty_field(json_data['product_name'], json_data['description'],
                         json_data['quantity'], json_data['price']):
        return make_response(jsonify({"message": "some fields are empty"}), 200)

    # checking whether correct data type has been passed in the field
    if check_types(product_name=json_data['product_name'], description=json_data['description'],
                   quantity=json_data['quantity'], price=json_data['price']):
        return make_response(jsonify({"message": "invalid types"}), 200)
    # checking for white spaces in the field
    if check_remove_white_spaces(json_data['product_name'], json_data['description']):
        return make_response(jsonify({"message": "white spaces not allowed"}), 200)

    product.create_product(json_data['product_name'], json_data['description'],
                           json_data['quantity'], json_data['price'])
    return make_response(jsonify({'message': "product created successfully "}), 200)
