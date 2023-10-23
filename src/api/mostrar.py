from config.db import db, app, ma
from flask import Blueprint, Flask, session, render_template, request,jsonify,json
from flask_sqlalchemy import SQLAlchemy
from model.login import logins


routes_mostrar = Blueprint("routes_mostrar", __name__)


@routes_mostrar.route('/mostrar_usuarios', methods=['GET'])
def mostrar_usuarios():
    datos = {}
    resultado = db.session.query(logins).select_from(logins).all()
 
    i = 0
    goria = []
    for cate in resultado:
        i += 1	       
        datos[i] = {
            'id': cate.id,
            'usuario': cate.usuario,
            'Email': cate.Email	,
            'contraseña': cate.contraseña,
            'sexo': cate.sexo,                                                                                                      
            'fecha_nacimiento': cate.fecha_nacimiento                                                
                                                          
        }
        goria.append(datos)
    return jsonify(datos)