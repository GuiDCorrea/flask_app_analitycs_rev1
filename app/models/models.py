from flask import Flask
from flask_sqlalchemy import SQLAlchemy



from ..extensions import db



class Usuario(db.Model):
    __schema__ = "comercial"
    __tablename__ = "usuarios"

    cod_usuario = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(700))
    uf = db.Column(db.String(3))
    cidade = db.Column(db.String(200))
    logradouro = db.Column(db.String(1000))
    data_atualizado = db.Column(db.DateTime, server_default=db.func.getdate())
    bitlogado = db.Column(db.Boolean)
    bitoff = db.Column(db.Boolean)
    bitativo = db.Column(db.Boolean)
    data_ultimo_login = db.Column(db.DateTime, server_default=db.func.getdate())

class Produto(db.Model):
    __schema__ = "comercial"
    __tablename__ = "produtos"

    cod_produto = db.Column(db.Integer, primary_key=True)
    nome_produto = db.Column(db.String)
    url_imagem = db.Column(db.String)
    marca = db.Column(db.String(200))
    categoria = db.Column(db.String(100))
    departamento = db.Column(db.String(100))
    subcategoria = db.Column(db.String(100))
    cor = db.Column(db.String(200))
    fator_caixa = db.Column(db.Float)
    grupo = db.Column(db.String(200))
    atributos = db.Column(db.String)
    url_pagina = db.Column(db.String)
    cod_google = db.Column(db.Integer)
    data_atualizado = db.Column(db.DateTime, server_default=db.func.getdate())

class GoogleShopping(db.Model):
    __schema__ = "comercial"
    __tablename__ = "googleshopping"

    cod_google = db.Column(db.Integer, primary_key=True)
    ean = db.Column(db.String(30))
    nome_produto = db.Column(db.String(400))
    url_gogle = db.Column(db.String)
    url_anuncio = db.Column(db.String)
    preco = db.Column(db.Float)
    seller = db.Column(db.String(100))
    preco_infos = db.Column(db.String(20))
    data_atualizado = db.Column(db.DateTime, server_default=db.func.getdate())
    cod_produto = db.Column(db.Integer, db.ForeignKey('comercial.produtos.cod_produto'))

class Pedido(db.Model):
    __schema__ = "comercial"
    __tablename__ = "pedidos"

    cod_pedido = db.Column(db.Integer, primary_key=True)
    cod_usuario = db.Column(db.Integer, db.ForeignKey('comercial.usuarios.cod_usuario'))
    cod_produto = db.Column(db.Integer, db.ForeignKey('comercial.produtos.cod_produto'))
    quantidade = db.Column(db.Float)
    preco = db.Column(db.Float)
    preco_total = db.Column(db.Float)

class TreinoProduto(db.Model):
    __schema__ = "comercial"
    __tablename__ = "treino_produto"

    cod_treino = db.Column(db.Integer, primary_key=True)
    cod_usuario = db.Column(db.Float)
    cod_produto = db.Column(db.Integer, db.ForeignKey('comercial.produtos.cod_produto'))
    cod_google = db.Column(db.Integer, db.ForeignKey('comercial.googleshopping.cod_google'))
    rating_ALS = db.Column(db.Float)
    lift = db.Column(db.Float)
    confianca = db.Column(db.Float)
    suport = db.Column(db.Float)
    rating = db.Column(db.Float)



'''

from datetime import datetime, timedelta, timezone
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token, get_jwt, jwt_required, JWTManager

app = Flask(__name__)



class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    type = db.Column(db.String(16), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()

    return token is not None


@app.route("/login", methods=["POST"])
def login():
    access_token = create_access_token(identity="example_user")
    return jsonify(access_token=access_token)

@app.route("/logout", methods=["DELETE"])
@jwt_required(verify_type=False)
def logout():
    token = get_jwt()
    jti = token["jti"]
    ttype = token["type"]
    now = datetime.now(timezone.utc)
    db.session.add(TokenBlocklist(jti=jti, type=ttype, created_at=now))
    db.session.commit()
    return jsonify(msg=f"{ttype.capitalize()} token successfully revoked")

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    return jsonify(hello="world")

if __name__ == "__main__":
    db.create_all()
    app.run()
'''