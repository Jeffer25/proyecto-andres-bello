from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo

class UserForm(FlaskForm):
    username = IntegerField('Usuario', validators = [DataRequired()], render_kw = {"placeholder":"Usuario"})
    password = PasswordField('Contraseña', validators = [DataRequired()],
                                                        render_kw = {"placeholder":"Contraseña"})
    names = StringField('Nombres', validators = [DataRequired()], render_kw = {"placeholder":"Nombres"})
    lastnames = StringField('Apellidos', validators = [DataRequired()], render_kw = {"placeholder":"Apellidos"})
    email = EmailField('Correo', validators = [DataRequired()], render_kw = {'placeholder':'Correo'})
    phone = IntegerField('Telefono', validators = [DataRequired()], render_kw = {'placeholder':'Telefono'})
    submit = SubmitField('Registrarse')