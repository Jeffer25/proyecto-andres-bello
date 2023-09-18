from flask import g, request, flash, redirect, url_for, render_template
from app import app
from modelo.mod_database import db
from modelo.mod_agregar_estudiante_forms import EstudianteForm
from modelo.mod_agregar_estudiante import Estudiante
from modelo.mod_agregar_representante import Representante
from modelo.mod_grado_seccion import GradoSeccion


@app.route("/registrar_representante/<int:cedula><repNombre>_<repApellido>/registrar_estudiante", methods = ["GET", "POST"])
def registrar_estudiante(cedula,repNombre,repApellido):
	if g.user:
		estudiante = Estudiante()
		estudianteForm = EstudianteForm(obj = estudiante)
		representante = Representante.query.get_or_404(cedula)
		if request.method == 'POST':
			if estudianteForm.validate_on_submit():
				nuevo_estudiante = Estudiante(representante_id = cedula, cod_grado_seccion = estudianteForm.curso.data)
				estudianteForm.populate_obj(nuevo_estudiante)
				app.logger.debug(f'Estudiante a Registrar: {nuevo_estudiante}')
				#insertamos el nuevo registro
				db.session.add(nuevo_estudiante)
				db.session.commit()
				flash("Estudiante registrado exitosamente.", "alert-success")
				return redirect(url_for("home"))
			else:
				flash("algo anda mal.", "alert-warning")

		return render_template("vis_agregar_estudiante.html", formaEst = estudianteForm, repNombre = repNombre, repApellido = repApellido)
	flash("Ya te encuentras con la sesion iniciada.", "alert-primary") 
	return redirect(url_for("home"))