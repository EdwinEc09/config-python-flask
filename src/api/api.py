from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from model.tabla1 import tabla1
from werkzeug.security import generate_password_hash , check_password_hash

routes_login = Blueprint("routes_login", __name__)



# este es una prueba(ejemplo) de como va el api 
@routes_login.route('/login', methods=['POST'])
def validar_login():
    usuario = request.json["usuario"]
    contraseña = request.json["contraseña"]
    verificacion = db.session.query(admins).filter(admins.correo == usuario).first()
    if verificacion:
        admin_id = verificacion.id  # Obtener el ID del administrador
        admin_nombre = verificacion.nombre  # Obtener el nombre del administrador
        if check_password_hash(verificacion.contraseña, contraseña):
            session["admin_id"] = admin_id  # Guardar el admin_id en la sesión
            session["admin_nombre"] = admin_nombre  # Guardar el nombre del administrador en la sesión
            return {"status": "Correcto", "message": "Inicio de sesión exitoso"}
        else:
            return {"status": "Error", "message": "Contraseña incorrecta"}
    else:
        return {"status": "Error", "message": "Correo incorrecto"}
    
    