from flask import Flask
from config import config
from .apiv1 import api_blueprint as api_blueprint


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_blueprint(api_blueprint, url_prefix="/api/v1")
    return app
