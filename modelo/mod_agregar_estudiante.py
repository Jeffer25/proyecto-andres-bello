from modelo.mod_database import db
from modelo.mod_agregar_representante import Representante
from modelo.mod_asigna import Asigna
from modelo.mod_cursa import Cursa


class Estudiante(db.Model):
	cedula = db.Column(db.Integer, primary_key = True)
	responsable = db.Column(db.String(60), nullable = False)
	tipo_inscrip = db.Column(db.String(30), nullable = False)
	antecedente_escolar = db.Column(db.String(30), nullable = False)
	nombres = db.Column(db.String(60), nullable = False)
	apellidos = db.Column(db.String(60), nullable = False)
	genero = db.Column(db.String(15), nullable = False)
	nacionalidad = db.Column(db.String(15), nullable = False)
	lugar_naci = db.Column(db.String(200), nullable = False)
	fecha_naci = db.Column(db.Date, nullable = False)
	parto = db.Column(db.String(200), nullable = False)
	edad = db.Column(db.Integer, nullable = False)
	lateralidad = db.Column(db.String(30), nullable = False)
	lugar_naci = db.Column(db.String(200), nullable = False)
	peso = db.Column(db.Float, nullable = False)
	estatura = db.Column(db.Float, nullable = False)
	hermanos = db.Column(db.String(20), nullable = False)
	hermanos_inst = db.Column(db.String(20), nullable = False)
	talla_camisa = db.Column(db.String(10), nullable = False)
	talla_pantalon = db.Column(db.String(10), nullable = False)
	salud = db.Column(db.String(50), nullable = False)
	covid = db.Column(db.String(20), nullable = False)
	vacunas_covid = db.Column(db.String(50), nullable = False)
	atencion_espec = db.Column(db.String(50), nullable = False)
	email_estud = db.Column(db.String(254), nullable = False)
	equipo_tecn = db.Column(db.String(50), nullable = False)
	acceso_inter = db.Column(db.String(200), nullable = False)
	redes_soc = db.Column(db.String(200), nullable = False)
	canaima = db.Column(db.String(10), nullable = False)
	#Relación entre estudiante y representante 1:M
	representante_id = db.Column(db.Integer, db.ForeignKey('representante.cedula'))
	representante = db.relationship('Representante', backref = db.backref('estudiantes', lazy = True))
	#Relación entre estudiante y grado_seccion 1:M
	cod_grado_seccion = db.Column(db.Integer, db.ForeignKey('grado_seccion.cod_grado_seccion'))
	grado_seccion = db.relationship('GradoSeccion', backref = db.backref('estudiantes', lazy = True))


	# #relacion M:M con materia
	# materias =  db.relationship('Materia', secondary = 'cursa')

	def __str__(self):
		return (
            f'Cedula: {self.cedula},'
            f'Nombres: {self.nombres},'
            f'Apellidos: {self.apellidos},'
            f'Edad: {self.edad},'
            f'Representante: {self.representante_id},'
			f'Grado id: {self.cod_grado_seccion}'
        )