from modelo.mod_database import db
from modelo.mod_asigna import Asigna
from modelo.mod_imparte import Imparte
#from modelo.mod_profesor import Profesor

class GradoSeccion(db.Model):
    __tablename__ = 'grado_seccion'
    cod_grado_seccion = db.Column(db.Integer, nullable = False, primary_key = True)
    grado_seccion = db.Column(db.String(50), nullable = False)
    
    #relacion M:M con profesor
    profesores =  db.relationship('Profesor', secondary = 'asigna')
    
    #relacion M:M con materias
    materias =  db.relationship('Materia', secondary = 'imparte')

    def __str__(self):
        return (
            f'{self.grado_seccion}'
        )