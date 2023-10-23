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

    
@routes_login.route('/guardaregistros', methods=['POST'])
def guardaregistross():

    regis_usuario = request.form['regis_usuarioss']
    print(regis_usuario)
    email = request.form['email']
    contrasena = request.form['contrasena']
    sexo = request.form['sexo']
    fecha_nacimiento = request.form['fecha_nacimiento']

    # Verificar si el usuario o el email ya existen en la base de datos
    existing_user = logins.query.filter(logins.usuario == regis_usuario).first()
    existing_email = logins.query.filter(logins.Email == email).first()
    if existing_user:
        return "Usuario ya existe"
    if existing_email:
        return "Email ya existe"
    
    # Si no existen ni el usuario ni el email, crea una nueva entrada
    new_reg = logins(regis_usuario, email,contrasena, sexo, fecha_nacimiento)
    db.session.add(new_reg)
    db.session.commit()
    return "Registro exitoso"
