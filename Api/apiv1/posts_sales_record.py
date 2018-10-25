from Api.modules.sales_record import SalesRecord
from flask import jsonify, make_response, request
from ..apiv1 import api_blueprint


@api_blueprint.route('/sales', methods=['POST'])
def post_sales_record():
    """endpoint for creating a sales records products"""
    json_data = request.get_json(force=True)
    sales = SalesRecord()
    sales.create_sales_records(attendant_name=json_data['attendant_name'], product_name=json_data['product'],
                               quantity=json_data['quantity'], unit_price=json_data['unit_price'])
    return make_response(jsonify({'message': 'records created successfully'}), 201)