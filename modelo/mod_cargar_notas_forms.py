from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class NotaForm(FlaskForm):
    nota1 = IntegerField('Nota 1', validators = [DataRequired()], render_kw = {"placeholder":"1ra Nota"})
    nota2 = IntegerField('Nota 2', validators = [DataRequired()], render_kw = {"placeholder":"2da Nota"})
    nota3 = IntegerField('Nota 3', validators = [DataRequired()], render_kw = {"placeholder":"3ra Nota"})
    promedio = IntegerField('Promedio', validators = [DataRequired()], render_kw = {"placeholder":"Promedio"})
    submit = SubmitField('Cargar Notas')