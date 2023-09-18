from modelo.mod_database import db
from modelo.mod_agregar_estudiante import Estudiante
from modelo.mod_profesor import Profesor
from modelo.mod_materia import Materia

#crear las tablas de materia y profesor
class Nota(db.Model):
    cod_nota = db.Column(db.Integer, nullable = False, primary_key = True)
    nota_1er_lapso = db.Column(db.Integer, nullable = False)
    nota_2do_lapso = db.Column(db.Integer, nullable = False)
    nota_3er_lapso = db.Column(db.Integer, nullable = False)
    promedio = db.Column(db.Integer, nullable = False)

    #Relacion con estudiante 1:M
    ced_estudiante = db.Column(db.Integer, db.ForeignKey('estudiante.cedula'))
    estudiante = db.relationship('Estudiante', backref = db.backref('notas', lazy = True))

    #Relacion con Materia 1:M
    cod_materia = db.Column(db.String(10), db.ForeignKey('materia.cod_materia'))
    materia = db.relationship('Materia', backref = db.backref('notas', lazy = True))
    
    #Relacion con profesor 1:M
    cedula_prof = db.Column(db.Integer, db.ForeignKey('profesor.cedula_prof'))
    profesor = db.relationship('Profesor', backref = db.backref('notas'), lazy = True)


