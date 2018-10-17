from flask import Blueprint

api_blueprint = Blueprint('api_blueprint', __name__)

from . import get_single_product_endpoints
