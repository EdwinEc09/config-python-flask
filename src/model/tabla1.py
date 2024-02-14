from config.db import db, app, ma 

class tabla1(db.Model):
    __tablename__ = "tbl1"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    id_admin = db.Column(db.Integer, db.ForeignKey('tbladmin.id'), nullable=True)

    def __init__(self, name,  id_admin=None):
        self.name = name
        self.id_admin = id_admin

with app.app_context():
    db.create_all() 