from config.db import db, app, ma
from flask import Blueprint, Flask, session, render_template
from flask_sqlalchemy import SQLAlchemy


routes_home = Blueprint("routes_home", __name__)


@routes_home.route("/index_dashboar",  methods=['GET'])
def index_dashboar():
    titulo = "Pagina cita"
    return render_template('/main/index.html', titles=titulo)

@routes_home.route("/index_registro",  methods=['GET'])
def index_registro():
    titulo = "Pagina registro"
    return render_template('/main/registro.html', titles=titulo)

@routes_home.route("/index_login",  methods=['GET'])
def index_login():
    titulo = "Pagina login"
    return render_template('/main/login.html', titles=titulo)

@routes_home.route("/index_citas",  methods=['GET'])
def index_citas():
    titulo = "Pagina citas"
    return render_template('/main/citas.html', titles=titulo)

@routes_home.route("/index_pacientes",  methods=['GET'])
def index_pacientes():
    titulo = "Pagina "
    return render_template('/main/pacientes.html', titles=titulo)



# #   este es un ejemplo de como protejer las rutas con session
# @routes_home.route("/perfil" , methods=['GET'] )
# def perfil():
#     usuario_sessio = session.get("usuario_sessio")
#     if usuario_sessio:
#         return render_template('/main/perfil.html')
#     else:
#         return render_template('/main/login_admin.html')


 




