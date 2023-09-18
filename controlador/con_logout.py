from app import *
# from flask import Flask
# app = Flask(__name__)

@app.route("/logout")
def logout():
    session.pop("Usuario", None)
    flash("Has cerrado sesion.", "alert-secondary")

    return redirect(url_for("login"))