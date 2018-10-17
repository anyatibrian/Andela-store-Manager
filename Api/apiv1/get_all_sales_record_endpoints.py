from Api.modules.sales_record import sales_records
from flask import jsonify, make_response

from Api.apiv1 import api_blueprint


@api_blueprint.route('/sales', methods=['GET'])
def get_sales_records():
    if len(sales_records) != 0:
        return make_response(jsonify({'message': sales_records}))
    else:
        return make_response(jsonify({'records': 'you dont have any sales record yet'}))
