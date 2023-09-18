from flask import g, flash, redirect, url_for, render_template
from modelo.mod_materia import Materia
from modelo.mod_grado_seccion import GradoSeccion
from modelo.mod_imparte import Imparte
from app import app


# Crear un controlador para la carga de notas de un estudiante llamada ...
@app.route('/ver_notas_secciones/<int:cod_grado>/ver_notas_materias')
def ver_notas_materias(cod_grado):
	if g.user:
		materias = Materia.query.order_by('cod_materia').join(Imparte.query.filter_by(cod_grado_seccion = cod_grado))
		
		
		for materia in materias:
			app.logger.debug(f'materia: {materia.nom_materia}')
		return render_template("vis_ver_notas_materias.html", materias = materias)
	flash("Primero debes iniciar sesion.", "alert-warning")

	return redirect(url_for("login"))