from modelo.mod_database import db

class User(db.Model):
	username = db.Column(db.Integer, primary_key = True)
	password = db.Column(db.String(100), nullable = False)
	names = db.Column(db.String(50), nullable = False)
	lastnames = db.Column(db.String(50), nullable = False)
	email = db.Column(db.String(254), nullable = False)
	phone = db.Column(db.BigInteger, nullable = False)


	def __str__(self):
		return (
            f'\nUsuario: {self.username},\n'
            f'contraseña: {self.password},\n'
            f'Nombres: {self.names},\n'
            f'Apellidos: {self.lastnames},\n'
            f'Correo: {self.email},\n'
            f'Telefono: {self.phone}\n'
        )

	