#https://docs.sqlalchemy.org/en/14/core/type_basics.html
#https://flask.palletsprojects.com/en/2.2.x/
#from api.user import *
from flask import Flask ,session, render_template
from config.db import db, app, ma


# #importar los model en orden
# from model.login import logins
# from model.odontologo1 import odontologos1



# importar los model en orden
from model.admin import admins
from model.paciente import pacientes
from model.odontologo import odontologos
from model.histo_clinico import histoclinicos
from model.fechas_disponibles import  fechas_disponi
from model.cita import citas
from model.tratamiento import tratamientos



# importacion de los api
# from api.login import routes_login
# app.register_blueprint(routes_login, url_prefix="/api")

# from api.mostrar import routes_mostrar
# app.register_blueprint(routes_mostrar, url_prefix="/api")

# importacion del home
from rutas.home import routes_home
app.register_blueprint(routes_home, url_prefix="/fronted")



# esto es para la redireccion de la pagina cuando la ruta este mal
# @app.errorhandler(404)
# def not_found(error):
#     if 'conectado' in session:
#         return redirect(url_for('index'))
#     else:
#         return render_template('/main/login_admin.html')

@app.route("/")
def index():
    return render_template('/main/login.html')




#esto para que corra el server y ayuda con el puerto
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    
    
    
    
    
    
    


