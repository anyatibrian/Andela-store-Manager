from flask import Blueprint

api_blueprint = Blueprint('api_blueprint', __name__)
from . import get_single_product, get_all_products, posts_product, posts_sales_record
