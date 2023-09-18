from flask import g, request, flash, redirect, url_for, render_template
from app import app
from modelo.mod_database import db
from modelo.mod_admin_forms import UserForm
from modelo.mod_admin import User
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/signup", methods = ["GET", "POST"])
def signup():
	if not g.user:
		user = User()
		userForm = UserForm(obj = user)
		if request.method == 'POST':
			#hashed_password = generate_password_hash(userForm.password.data, method = 'sha256')
			#new_user = User(password = generate_password_hash(userForm.password.data, method = 'sha256'))
			if userForm.validate_on_submit():
				#app.logger.debug(f'Contrasenia encriptada: {hashed_password}\n')
				#new_user = User(password = hashed_password)
				userForm.password.data = generate_password_hash(userForm.password.data, method = 'sha256')
				userForm.populate_obj(user)
				app.logger.debug(f'Persona a Registrar: {user}')
				#insertamos el nuevo registro
				db.session.add(user)
				db.session.commit()
				flash("Te has registrado exitosamente.", "alert-success")
				return redirect(url_for("login"))
			
		return render_template("vis_signup.html", forma = userForm)
	flash("Ya te encuentras con la sesion iniciada.", "alert-primary") 
	return redirect(url_for("home"))