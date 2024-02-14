from flask import Flask, render_template
from config.db import app, db, ma

# este es para importar el api
from api.api import route_login
#importar el home todas las rutas de las viustas del servidor
app.register_blueprint(route_login , url_prefix="/api")



# este es para importar el model(las tablas de la db) y va en orden dependiendo cuantas sean
from model.tabla1 import tabla1



#importar la ruta hoome 
from rutas.home import routes_home
#importar el home todas las rutas de las viustas del servidor
app.register_blueprint(routes_home , url_prefix="/fronted")



@app.route("/")
def index():
    # titulo= "Pagina Princiapl"
    # return render_template('/main/principal.html', titles=titulo)
    return render_template('/main/index.html')



# pagina no encontrada
@app.errorhandler(404)
def not_found(error):
    # return render_template('error.html'), 404
    return "pagina no encontrada",404



# este cierra sesion
# @app.route('/logout')
# def logout():
#     # Eliminar datos de sesión, esto cerrará la sesión del usuario
#     session.pop('conectado', None)
#     session.pop('admin_id', None)
#     session.pop('admin_nombre', None)

#     return redirect(url_for('index'))




# esto es casi lo mismo de arriba solo que aqui maneja proteccon por si el user no esta en la sesion
# @app.errorhandler(404)
# def not_found(error):
#     if 'conectado' in session:
#         return redirect(url_for('index'))
#     else:
#         return render_template('/main/principal.html')



#esto para que corra el server y ayuda con el puerto
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')