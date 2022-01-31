from flask import Flask
from db import db


def create_app() -> Flask:
    app = Flask(__name__)

    from api import api_bp

    api_bp.before_app_first_request(db.create_all)
    app.register_blueprint(api_bp)

    return app
