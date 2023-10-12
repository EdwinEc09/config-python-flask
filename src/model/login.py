from config.db import db, app, ma 
from werkzeug.security import generate_password_hash


class logins(db.Model):
    __tablename__ = "tbllogin"

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50))
    Email = db.Column(db.String(50))
    contraseña = db.Column(db.String(50))
    sexo = db.Column(db.String(50))
    fecha_nacimiento = db.Column(db.String(50))
    
    # id_admin = db.Column(db.Integer, db.ForeignKey('tbladmin.id'), nullable=True)

    def __init__(self,usuario,Email,contraseña ,sexo,fecha_nacimiento):
        # def __init__(self, Rol, fecha_de_regitro, Name, edad, cedula, telefono, direccion, Email, fecha_nacimiento, id_admin=None):
        self.usuario = usuario
        self.Email = Email
        self.contraseña = contraseña  # Generar el hash de la contraseña
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
         
        
   
        # self.id_admin = id_admin

with app.app_context():
    db.create_all() 
