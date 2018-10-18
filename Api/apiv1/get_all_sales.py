from Api.modules.sales_record import sales_records
from flask import jsonify, make_response

from Api.apiv1 import api_blueprint


@api_blueprint.route('/sales', methods=['GET'])
def get_sales_records():
    """getting all the  sales record from the list"""
    if len(sales_records) != 0:
        return make_response(jsonify({'records': sales_records}))
    else:
        return make_response(jsonify({'records': 'you dont have any sales record yet'}))