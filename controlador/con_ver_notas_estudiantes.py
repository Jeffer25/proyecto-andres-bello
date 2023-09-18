from flask import g, flash, redirect, url_for, render_template, request
from app import app
from modelo.mod_database import db
from modelo.mod_agregar_estudiante import Estudiante
from modelo.mod_cargar_notas import Nota
from modelo.mod_asigna import Asigna
from modelo.mod_imparte import Imparte
from modelo.mod_materia import Materia


# Crear un controlador para la carga de notas de un estudiante llamada ...
@app.route('/ver_notas_secciones/<int:cod_grado>/ver_notas_materias/<cod_materia>', methods = ['GET','POST'])
def ver_notas_estudiantes(cod_grado,cod_materia):
	if g.user:
		
		# estudiantes = Nota.query.order_by('cod_nota').join(Asigna, Nota.ced_estudiante == Asigna.ced_estudiante)
		estudiantes = Estudiante.query.order_by('cedula').join(Nota.query.filter_by(cod_materia = cod_materia)).join(Asigna.query.filter_by(cod_grado_seccion = cod_grado)).join(Nota.query.order_by('cod_nota'))
		notas = Nota.query.order_by('cod_nota').join(Materia.query.filter_by(cod_materia = cod_materia)).join(Estudiante.query.filter_by(cod_grado_seccion = cod_grado))
		for estudiante in estudiantes:
			app.logger.debug(f'{estudiante.nombres} ')
			app.logger.debug(f'{estudiante.apellidos}\n')
   
	
		return render_template("vis_ver_notas_estudiantes.html", estudiantes = estudiantes, notas = notas)
		flash("Primero debes iniciar sesion.", "alert-warning")

	return redirect(url_for("login"))

