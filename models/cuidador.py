from db import db

class Cuidadores(db.Model):
    
    id = db.Column(db.Integer,primary_key=True)
    nombre =  db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable = False) 
    id_guarderia = db.Column(db.Integer,db.ForeignKey("guarderias.id"),nullable=False)

    perro = db.relationship ('Perros',backref = "cuidadores",lazy = True)

    def setNombre(self, nombre):
        self.nombre = nombre
        db.session.commit()
