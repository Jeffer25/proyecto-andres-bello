from modelo.mod_database import db

class Imparte(db.Model):
    __tablename__ = 'imparte'
    cod_imparte = db.Column(db.Integer, nullable = False, primary_key = True)
    cod_materia = db.Column(db.String(10), db.ForeignKey('materia.cod_materia'), primary_key = True)
    cod_grado_seccion = db.Column(db.Integer, db.ForeignKey('grado_seccion.cod_grado_seccion'), primary_key = True)
    