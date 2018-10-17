from Api.modules.sales_record import sales_records
from  flask import make_response, jsonify
from Api.apiv1 import api_blueprint


@api_blueprint.route('/sales/<int:record_id>', methods=['GET'])
def get_single_records(record_id):
    if 0 < record_id < len(sales_records):
        sale = [sale for sale in sales_records if sale['id'] == record_id]
        return make_response(jsonify({'sales': sale[0]}))
    else:
        return make_response(jsonify({'message': 'such a record does not exit'}))