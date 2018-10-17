from flask import Blueprint

api_blueprint = Blueprint('api_blueprint', __name__)

from . import post_sales_records_endpoint
