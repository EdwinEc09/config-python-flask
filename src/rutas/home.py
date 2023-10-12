from config.db import db, app, ma
from flask import Blueprint, Flask, session, render_template
from flask_sqlalchemy import SQLAlchemy


routes_home = Blueprint("routes_home", __name__)


# @routes_home.route("/registro",  methods=['GET'])
# def indexregistro():
#     titulo = "Pagina cita"
#     return render_template('/main/registro_user.html', titles=titulo)



# #   este es un ejemplo de como protejer las rutas con session
# @routes_home.route("/perfil" , methods=['GET'] )
# def perfil():
#     usuario_sessio = session.get("usuario_sessio")
#     if usuario_sessio:
#         return render_template('/main/perfil.html')
#     else:
#         return render_template('/main/login_admin.html')


 




