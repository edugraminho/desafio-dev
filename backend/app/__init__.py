from flask import Flask
from environs import Env

from app.views.cnba_views import bp
from app.models.cnba_models import db, mg, ma
from config import DATA_PATH
import os 
from flask_cors import CORS


def create_app():
    env = Env()
    env.read_env()
    app = Flask(__name__)

    cors = CORS(app)

    app.secret_key = os.urandom(24)

    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['UPLOAD_FOLDER'] = DATA_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = env.bool("SQLALCHEMY_TRACK_MODIFICATIONS")
    app.config["SQLALCHEMY_DATABASE_URI"] = env.str("SQLALCHEMY_DATABASE_URI")

    db.init_app(app)
    mg.init_app(app, db)
    ma.init_app(app)

    app.register_blueprint(bp)

    return app