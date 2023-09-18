from modelo.mod_database import db


#Relación M:M con estudiante profesor y gradoSeccion
class Asigna(db.Model):
	"""docstring for ClassName"""
	__tablename__ = 'asigna'
	cod_asignar = db.Column(db.Integer, nullable = False, primary_key = True)
	ced_estudiante = db.Column(db.Integer, db.ForeignKey('estudiante.cedula'), primary_key = True)
	cedula_prof = db.Column(db.Integer, db.ForeignKey('profesor.cedula_prof'), primary_key = True)
	cod_grado_seccion = db.Column(db.Integer, db.ForeignKey('grado_seccion.cod_grado_seccion'), primary_key = True)
	cod_materia = db.Column(db.String(10), db.ForeignKey('materia.cod_materia'), primary_key = True)


		
