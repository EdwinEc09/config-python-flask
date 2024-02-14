from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from flask_sqlalchemy import SQLAlchemy


routes_home = Blueprint("routes_home", __name__)



# este es una prueba de como va el decorador y el objeto
@routes_home.route("/indexprueba",  methods=['GET'])
def indexprueba():
    # titulo = "Pagina prueba"
    # return render_template('/main/indexprueba.html', titles=titulo)
    return "index prueba ome care chimba desde el home.py"



# este es una referncia de como va la ruta con la session protegida
@routes_home.route("/indexrueba2" )
def indexprueba2():
    admin_nombre = session.get("admin_nombre")  # Obtener el nombre del administrador de la sesión
    titulo= "Pagina cita2"
    if admin_nombre:
        return render_template('/main/tablaadmin.html', titles=titulo,admin_nombre=admin_nombre)
    else:
        return render_template('/main/login_admin.html')