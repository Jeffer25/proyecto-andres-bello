from modelo.mod_database import db
from modelo.mod_profesor import Profesor
from modelo.mod_imparte import Imparte
#from modelo.mod_cursa import Cursa

class Materia(db.Model):
    __tablename__ = 'materia'
    cod_materia = db.Column(db.String(10), nullable = False, primary_key = True)
    nom_materia = db.Column(db.String(50), nullable = False)
    cedula_prof = db.Column(db.Integer, db.ForeignKey('profesor.cedula_prof'))
    
    #relacion entre materia y profesor 1:M
    profesor = db.relationship('Profesor', backref = db.backref('materias'), lazy = True)
    
    # #relacion M:M con grado_seccion
    grado_secciones =  db.relationship('GradoSeccion', secondary = 'imparte')
    
    def __str__(self):
        return (
            f'Codigo materia: {self.cod_materia},'
            f'Nombre de Materia: {self.nom_materia},'
        )