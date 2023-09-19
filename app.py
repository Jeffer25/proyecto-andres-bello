from flask import Flask, render_template, request, session, redirect, url_for, flash, g
from flask_migrate import Migrate
from modelo.mod_database import db
from werkzeug.security import generate_password_hash, check_password_hash

# import os

app = Flask(__name__)

# Configuración de la base de datos
USER_DB = "postgres"
PASS_DB = "admin"
URL_DB = "localhost"
NAME_DB = "pab_db"
FULL_URL_DB = f"postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}"

app.config["SQLALCHEMY_DATABASE_URI"] = FULL_URL_DB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Configurar flask-migrate
migrate = Migrate()
migrate.init_app(app, db)

# Configuración de flask-wtf
app.config["SECRET_KEY"] = "Mi_llave_secreta"

from controlador.con_home import *
from controlador.con_login import *
from controlador.con_admin import *
from controlador.con_logout import *
from controlador.con_consultar_estudiante import *
from controlador.con_consultar_estudiantes import *
from controlador.con_agregar_estudiante import *
from controlador.con_agregar_representante import *
from controlador.con_agregar_representante import *
from controlador.con_modificar_estudiante import *
from controlador.con_cargar_notas_secciones import *
from controlador.con_cargar_notas_materias import *
from controlador.con_cargar_notas_estudiantes import *
from controlador.con_ver_notas_secciones import *
from controlador.con_ver_notas_materias import *
from controlador.con_ver_notas_estudiantes import *


@app.before_request
def before_request():
    if "Usuario" in session:
        g.user = session["Usuario"]
    else:
        g.user = None


@app.route("/recuperacionContraseña", methods=["GET", "POST"])
def recovery():
    return render_template("vis_recuperacion_contraseña.html")


# Pasar esto al controlador y eliminarlo de aqui
"""@app.route('/cargar_notas')
def cargar_notas():
	if g.user:
		return render_template("vis_cargar_notas.html")
	flash("Primero debes iniciar sesion.", "alert-warning")

	return redirect(url_for("login"))
"""


@app.errorhandler(404)
def page_not_found(error):
    return render_template("vis_404_not_found.html"), 404
