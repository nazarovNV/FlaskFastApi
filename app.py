from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models import db, bcrypt
from routes import routes
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    Migrate(app, db)
    JWTManager(app)

    app.register_blueprint(routes)

    return app
