from flask import g, flash, redirect, url_for, render_template
from modelo.mod_agregar_estudiante import Estudiante
from app import app


@app.route('/consultar_estudiante/<int:cedula>')
def consultar_estudiante(cedula):
	if g.user:
		estudiante = Estudiante.query.get_or_404(cedula)
		app.logger.debug(f'Ver estudiante: {estudiante}')
		return render_template("vis_consultar_estudiante.html", estudiante = estudiante)
	flash("Primero debes iniciar sesion.", "alert-warning")

	return redirect(url_for("login"))