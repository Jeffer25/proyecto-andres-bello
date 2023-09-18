from flask import g, request, session, flash, redirect, url_for, render_template
from modelo.mod_admin import User
from app import app
from werkzeug.security import check_password_hash


@app.route("/login", methods = ["GET", "POST"])
@app.route('/', methods = ['GET', 'POST'])
def login():
	if not g.user:
		#Recuperamos los datos del usuario
		user = User()
		if request.method == "POST":
			user = User.query.filter_by(username = request.form["Usuario"]).first()
			if user and check_password_hash(user.password, request.form['Contraseña']):
				session["Usuario"] = user.username
				flash("Has iniciado sesion.", "alert-success")
				#Mostramos los datos del usuario que ha hecho login
				app.logger.debug(f'\nUsuario: {user.username}\nContraseña: {user.password}')
				return redirect("home")
			flash("Tus datos son invalidos, intentalo nuevamente.", "alert-warning")

		return render_template("vis_login.html")

	flash("Ya te encuentras logeado.", "alert-primary")
	return redirect(url_for("home"))
