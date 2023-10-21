#https://docs.sqlalchemy.org/en/14/core/type_basics.html
#https://flask.palletsprojects.com/en/2.2.x/
#from api.user import *
from flask import Flask ,session, render_template
from config.db import db, app, ma


# #importar los model en orden
from model.login import logins

# # importacion del home
# from rutas.home import routes_home
# app.register_blueprint(routes_home, url_prefix="/fronted")



# esto es para la redireccion de la pagina cuando la ruta este mal
# @app.errorhandler(404)
# def not_found(error):
#     if 'conectado' in session:
#         return redirect(url_for('index'))
#     else:
#         return render_template('/main/login_admin.html')
    
    
@app.route("/")
def index():
    return render_template('/main/index.html')




#esto para que corra el server y ayuda con el puerto
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    
    
    
    
    
    
    


