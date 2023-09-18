from modelo.mod_database import db


#relacion M:M con estudiante y materia
class Cursa(db.Model):
	__tablename__ = 'cursa'
	cod_cursa = db.Column(db.Integer, nullable = False, primary_key = True)
	cedula_estudiante = db.Column(db.Integer, db.ForeignKey('estudiante.cedula'), primary_key = True)
	cod_materia = db.Column(db.String(10), db.ForeignKey('materia.cod_materia'), primary_key = True)