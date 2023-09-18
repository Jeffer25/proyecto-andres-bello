from flask import g, flash, redirect, url_for, render_template, request
from app import app
from modelo.mod_database import db
from modelo.mod_agregar_estudiante import Estudiante
from modelo.mod_cargar_notas import Nota
from modelo.mod_cargar_notas_forms import NotaForm
from modelo.mod_asigna import Asigna
from modelo.mod_materia import Materia


# Crear un controlador para la carga de notas de un estudiante llamada ...
@app.route('/cargar_notas_secciones/<int:cod_grado>/cargar_notas_materias/<cod_materia>', methods=['GET', 'POST'])
def cargar_notas_estudiantes(cod_grado, cod_materia):
    if g.user:
        nota = Nota()
        notaForm = NotaForm(obj=nota)
        estudiantes = Estudiante.query.filter_by(cod_grado_seccion=cod_grado)
        for estudiante in estudiantes:
            app.logger.debug(f'estudiante: {estudiante.cedula}\n')

        materia = Materia.query.get(cod_materia)
        asigna = Asigna.query.order_by('cod_asignar')
        asignar = Asigna()
        # cod_asigna = 1
        if request.method == 'POST':
            for estudiante in estudiantes:
                estudiante = estudiante.cedula
                promedio_est = (notaForm.nota1.data + notaForm.nota2.data + notaForm.nota3.data) / 3
                app.logger.debug(f'Promedio: {promedio_est}')

                
                if asignar.ced_estudiante == estudiante:
                    agg_nota = Nota.query.filter_by(ced_estudiante=estudiante).update(
                        {"nota_1er_lapso": notaForm.nota1.data,
                            "nota_2do_lapso": notaForm.nota2.data,
                            "nota_3er_lapso": notaForm.nota3.data,
                            "promedio": promedio_est})
                    db.session.commit()
                    app.logger.debug(f'Notas Modificadas:\n')
                    app.logger.debug(f'1ra nota: {agg_nota.nota_1er_lapso}\n')
                    app.logger.debug(f'2da nota: {agg_nota.nota_2do_lapso}\n')
                    app.logger.debug(f'3ra nota: {agg_nota.nota_3er_lapso}\n')
                    app.logger.debug(f'Promedio: {agg_nota.promedio}\n')
                    break

                
                agg_nota = Nota(ced_estudiante=estudiante, nota_1er_lapso=notaForm.nota1.data,
                                nota_2do_lapso=notaForm.nota2.data,
                                nota_3er_lapso=notaForm.nota3.data, promedio=promedio_est, cod_materia=cod_materia)
                db.session.add(agg_nota)
                db.session.commit()
                # agg_asigna = Asigna(cod_asignar = cod_asigna, ced_estudiante = estudiante, cod_grado_seccion = cod_grado,
                #         			cod_materia = cod_materia, cedula_prof = 12345)

                # este bucle vale ORO🔅🥇🏆 (llave primaria autoincrementable)
                # for asignar in asigna:
                #     if asignar:
                #         cod_asigna += 1
                #     else:
                        
                #         break
                # asigna.populate_obj(agg_nota)
                # asign = Asigna.query.get(cod_asigna).join(Estudiante.query.filter_by(cedula = estudiante))
                # db.session.delete(asign)
                # db.session.commit()

                agg_asigna = Asigna(ced_estudiante=estudiante, cod_grado_seccion=cod_grado,
                                    cod_materia=cod_materia, cedula_prof=12345)
                app.logger.debug(f'1ra nota: {agg_nota.nota_1er_lapso}\n')
                app.logger.debug(f'2da nota: {agg_nota.nota_2do_lapso}\n')
                app.logger.debug(f'3ra nota: {agg_nota.nota_3er_lapso}\n')
                app.logger.debug(f'Promedio: {agg_nota.promedio}\n')
                app.logger.debug(f'Cod Asigna: {agg_asigna.cod_asignar}\n')
                # db.session.add(agg_nota)
                db.session.add(agg_asigna)
                db.session.commit()
                    
            flash("Notas cargadas exitosamente.", "alert-success")
            return redirect(url_for('home'))

        return render_template("vis_cargar_notas_estudiantes.html", estudiantes=estudiantes, nota=notaForm,
                               materia=materia)
        flash("Primero debes iniciar sesion.", "alert-warning")

    return redirect(url_for("login"))
