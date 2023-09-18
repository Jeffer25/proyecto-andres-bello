from flask import g, render_template, flash, redirect, url_for
from app import app

# from flask import Flask
# app = Flask(__name__)

@app.route('/home')
def home():
	if g.user:
		return render_template("vis_home.html")
	flash("Primero debes iniciar sesion.", "alert-warning")

	return redirect(url_for("login"))