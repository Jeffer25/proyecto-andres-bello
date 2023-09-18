from flask import Flask, request, g, url_for, redirect, render_template, flash
from app import app
from modelo.mod_database import db
from modelo.mod_agregar_estudiante_forms import EstudianteForm
from modelo.mod_agregar_estudiante import Estudiante
from modelo.mod_grado_seccion import GradoSeccion


@app.route('/modificar_estudiante/<int:cedula>', methods=['GET', 'POST'])
def modificar_estudiante(cedula):
    #Recuperamos el objeto persona a editar 
    estudiante = Estudiante.query.get_or_404(cedula)
    estudianteForm= EstudianteForm(obj = estudiante)

    if request.method == 'POST':
        if estudianteForm.validate_on_submit():
            estudiante_Modif = Estudiante.query.filter_by(cedula = cedula).update({"cod_grado_seccion":estudianteForm.curso.data})
            #estudiante_Modif = Estudiante(cod_grado_seccion = estudianteForm.curso.data)
            estudianteForm.populate_obj(estudiante)
            app.logger.debug(f'Estudiante a actualizar: {estudiante}')
            
            db.session.commit()
            flash('Estudiante modificado con exito.', 'alert-success')
            return redirect(url_for('consultar_estudiantes'))
    return render_template('vis_modificar_estudiante.html', formaEst = estudianteForm)