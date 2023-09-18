from flask import g, request, flash, redirect, url_for, render_template
from app import app
from modelo.mod_database import db
from modelo.mod_agregar_representante_forms import RepresentanteForm
from modelo.mod_agregar_representante import Representante

#FALTA AGREGAR LA VISTA DE AGREGAR REPRESENTANTE
@app.route("/registrar_representante", methods = ["GET", "POST"])
def registrar_representante():
	if g.user:
		representante = Representante()
		representanteForm = RepresentanteForm(obj = representante)
		if request.method == 'POST':
			if Representante.query.get(representanteForm.cedula.data):
				flash("Representante ya registrado.", "alert-warning")
				
			elif representanteForm.validate_on_submit():
				representanteForm.populate_obj(representante)
				app.logger.debug(f'Persona a Registrar: {representante}')
				#insertamos el nuevo registro
				db.session.add(representante)
				db.session.commit()
				flash("Representante registrado exitosamente.", "alert-success")
				return redirect(url_for("registrar_estudiante", cedula = representante.cedula, repNombre = representante.nombre, repApellido = representante.apellido))
			
		return render_template("vis_agregar_representante.html", formaRep = representanteForm)
	flash("Ya te encuentras con la sesion iniciada.", "alert-primary") 
	return redirect(url_for("home"))