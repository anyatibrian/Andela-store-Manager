from flask import Flask
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # registering the blue print object
    from .apiv1 import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1/')
    return app
