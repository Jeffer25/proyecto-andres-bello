from flask import g, flash, redirect, url_for, render_template
from modelo.mod_agregar_estudiante import Estudiante
from app import app


# Crear un controlador para la carga de notas de un estudiante llamada ...
@app.route('/cargar_notas')
def cargar_notas():
	if g.user:
		estudiantes = Estudiante.query.order_by('cedula')
		total_estudiantes = Estudiante.query.count()
		app.logger.debug(f'Total Estudiantes: {total_estudiantes}')
		# for estudiante in estudiantes:
		# 	app.logger.debug(f'\nEstudiante: {estudiante.nombres}, Cedula:{estudiante.cedula} Responsable: {estudiante.representante_id}\n')
		return render_template("vis_cargar_notas_secciones.html", estudiantes = estudiantes)
	flash("Primero debes iniciar sesion.", "alert-warning")

	return redirect(url_for("login"))