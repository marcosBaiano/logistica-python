from flask import Flask

from config.config import Config

from app.database.db import db
from app.routes.chat_routes import chat_bp
from app.routes.admin_routes import admin_bp
from app.routes.api_routes import api_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(chat_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(api_bp, url_prefix='/api')

    with app.app_context():
        db.create_all()

    return app
