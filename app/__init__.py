
from datetime import timedelta
from flask import (Flask,flash, redirect, url_for,abort, jsonify, current_app)
from flask_sqlalchemy import SQLAlchemy
import secrets
import os
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from config import SQLALCHEMY_DATABASE_URI
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token, get_jwt, jwt_required, JWTManager


from .extensions import db


def create_app():

    app = Flask(__name__)
    
    ACCESS_EXPIRES = timedelta(hours=1)
    app.config["JWT_SECRET_KEY"] = "super-secret"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
    jwt = JWTManager(app)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    #app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.realpath('__file__')),'uploads')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_EXTENSIONS'] = ['.csv', '.xlsx', '.xls']
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

    db.init_app(app)

    
    with app.app_context():
        from .admin.admin import adminbp
        from .admin.Api import Api
        
        app.register_blueprint(Api)
        app.register_blueprint(adminbp)

 
    
    return app


