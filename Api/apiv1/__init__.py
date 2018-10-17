from flask import Blueprint

api_blueprint = Blueprint('api_blueprint', __name__)

from . import get_all_sales_record_endpoints
