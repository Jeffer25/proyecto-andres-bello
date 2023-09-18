from modelo.mod_database import db

#FALTA AGREGAR LA VISTA DE AGREGAR REPRESENTANTE
class Representante(db.Model):
    nombre = db.Column(db.String(60), nullable = False)
    apellido = db.Column(db.String(60), nullable = False)
    nacionalidad = db.Column(db.String(15), nullable = False)
    cedula = db.Column(db.Integer, nullable = False, primary_key = True)
    parentesco = db.Column(db.String(30), nullable = False)
    lugar_naci = db.Column(db.String(200), nullable = False)
    telefono = db.Column(db.BigInteger, nullable = False)
    telefono_alt = db.Column(db.BigInteger, nullable = False)
    profesion = db.Column(db.String(100), nullable = False)
    telefono_trab = db.Column(db.BigInteger, nullable = False)
    direccion_trab = db.Column(db.String(200), nullable = False)
    vive_chacao = db.Column(db.String(10), nullable = False)
    direccion_dom = db.Column(db.String(200), nullable = False)
    estado_viv_infra = db.Column(db.String(100), nullable = False)
    estado_viv_tipo = db.Column(db.String(100), nullable = False)
    estado_viv_cond = db.Column(db.String(100), nullable = False)
    resolucion_0 = db.Column(db.String(150), nullable = False)


    def __str__(self):
	    return (
            f'\nCedula: {self.cedula},\n'
            f'Nombre: {self.nombre},\n'
            f'Apellido: {self.apellido},\n'
            f'Parentesco: {self.parentesco},\n'
            f'Telefono: {self.telefono},\n'
        )