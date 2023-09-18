from modelo.mod_database import db
from modelo.mod_asigna import Asigna
#from modelo.mod_grado_seccion import GradoSeccion


class Profesor(db.Model):
	__tablename__ = 'profesor'
	cedula_prof = db.Column(db.Integer, primary_key = True)
	nombre = db.Column(db.String(50), nullable = False)
	apellido = db.Column(db.String(50), nullable = False)

	
	#relacion M:M con gradoSeccion
	grado_secciones =  db.relationship('GradoSeccion', secondary = 'asigna')
