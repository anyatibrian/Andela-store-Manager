from flask import Blueprint

api_blueprint = Blueprint('api_blueprint', __name__)
from . import posts_product, get_all_products, get_single_product
