from flask import Blueprint,redirect
from flask import Flask, jsonify
import json
import os

from sqlalchemy import select

from ..models.models import GoogleShopping

from ..extensions import db


Api = Blueprint("index",__name__)




@Api.route("/allsugestions/als")
def all_sugestions_als():
   with db.engine.connect() as connection:
    stmt = select(
        GoogleShopping.c.cod_google,
        GoogleShopping.c.url_google,
        GoogleShopping.c.concorrente,
        GoogleShopping.c.diferencaconcorrente
    )
    result = connection.execute(stmt).all()
    
    return 'jsonify()'




@Api.route("/")
def all_fpgrowth():
    return redirect('admin')
