from config.db import db, app, ma
from flask import Blueprint, Flask, session, render_template, request
from flask_sqlalchemy import SQLAlchemy
from model.login import logins


routes_login = Blueprint("routes_login", __name__)



@routes_login.route('/validar_login', methods=['POST'])
def validar_login():
    Email = request.json["usuario"]
    contraseña = request.json["contrasena"]
    verificacion = db.session.query(logins).filter(logins.Email == Email).first()
    if verificacion:
        admin_id = verificacion.id  # Obtener el ID del administrador
        
        if verificacion and verificacion.contraseña == contraseña:
            session["admin_id"] = admin_id  # Guardar el admin_id en la sesión
            return {"status": "Correcto", "message": "Inicio de sesión exitoso"}
        else:
            return {"status": "Error", "message": "Contraseña incorrecta"}
    else:
        return {"status": "Error", "message": "Correo incorrecto"}
    