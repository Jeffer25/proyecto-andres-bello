from flask import g, flash, redirect, url_for, render_template
from modelo.mod_grado_seccion import GradoSeccion
from app import app


# Crear un controlador para la carga de notas de un estudiante llamada ...
@app.route('/cargar_notas_secciones')
def cargar_notas_secciones():
	if g.user:
		grado_seccion = GradoSeccion.query.order_by('cod_grado_seccion')
		
		return render_template("vis_cargar_notas_secciones.html", grado_seccion = grado_seccion)
	flash("Primero debes iniciar sesion.", "alert-warning")

	return redirect(url_for("login"))