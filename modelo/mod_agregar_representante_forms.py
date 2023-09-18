from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, SubmitField, PasswordField, DateField, SelectField, FloatField
from wtforms.validators import DataRequired, Email

class RepresentanteForm(FlaskForm):
    nombre = StringField('Nombres', validators = [DataRequired()], render_kw = {"placeholder":"Nombres"})
    apellido = StringField('Apellidos', validators = [DataRequired()], render_kw = {"placeholder":"Apellidos"})
    nacionalidad = SelectField('Nacionalidad', validators = [DataRequired()], choices = [('Nacionalidad',0),('Venezolano(a)','Venezolano(a)'),('Extranjero(a)','Extranjero(a)')])
    cedula = IntegerField('Cedula', validators = [DataRequired()], render_kw = {"placeholder":"Cédula"})
    parentesco = SelectField('Parentesco', validators = [DataRequired()], choices = [('Parentesco',0),('Madre / Padre','Madre / Padre'),('Abuelo / Abuela','Abuelo / Abuela'),('Tío / Tía','Tío / Tía')])
    lugar_naci = StringField('Lugar de Nacimiento de la Madre - Estado', validators = [DataRequired()], render_kw = {"placeholder":"Lugar de Nacimiento de la Madre - Estado"})
    telefono = IntegerField('Número de telefono', validators = [DataRequired()], render_kw = {"placeholder":"Número de telefono"})
    telefono_alt = IntegerField('Número de telefono alternativo', validators = [DataRequired()], render_kw = {"placeholder":"Número de telefono alternativo"})
    profesion = StringField('Profesión/Ocupación', validators = [DataRequired()], render_kw = {"placeholder":"Profesión/Ocupación"})
    telefono_trab = IntegerField('Numero telefonico del trabajo', validators = [DataRequired()], render_kw = {"placeholder":"Numero telefonico del trabajo"})
    direccion_trab = StringField('Nombre y dirección de la Empresa', validators = [DataRequired()], render_kw = {"placeholder":"Nombre y dirección de la Empresa"})
    vive_chacao = SelectField('¿Vive en el Municipio Chacao?', validators = [DataRequired()], choices = [('¿Vive en el Municipio Chacao?',0),('Si','Si'),('No','No')])
    direccion_dom = StringField('Dirección de Domicilio', validators = [DataRequired()], render_kw = {"placeholder":"Dirección de Domicilio"})
    estado_viv_infra = SelectField('Estado de la Vivienda - Infraestructura', validators = [DataRequired()], choices = [('Estado de la Vivienda - Infraestructura',0),('Deplorable','Deplorable'),('Deteriorada','Deteriorada'),('Regular','Regular'),('Buena','Buena'),('Excelente','Excelente')])
    estado_viv_tipo = SelectField('Estado de la Vivienda - Tipo', validators = [DataRequired()], choices = [('Estado de la Vivienda - Tipo',0),('Apartamento','Apartamento'),('Aparto - Quinta','Aparto - Quinta'),('Casa','Casa'),('Casa de vecindad - Pensión','Casa de vecindad - Pensión'),('Casa - Quinta','Casa - Quinta'),('Improvisada','Improvisada'),('Quinta','Quinta'),('Rancho Rural','Rancho Rural'),('Rancho Urbano','Rancho Urbano'),('Refugio','Refugio')])
    estado_viv_cond = SelectField('Estado de la Vivienda - Condición', validators = [DataRequired()], choices = [('Estado de la Vivienda - Condición',0),('Al cuido','Al cuido'),('Alquilada','Alquilada'),('Anexo','Anexo'),('Arrimada/o','Arrimada/o'),('Cedida','Cedida'),('Conserjería','Conserjería'),('De la empresa','De la empresa'),('Herencia / Sucesión','Herencia / Sucesión'),('Indígena','Indígena'),('Invasión / Tomada','Invasión / Tomada'),('Prestada / Comodato','Prestada / Comodato'),('Propia pagada','Propia pagada'),('Propia pagándose','Propia pagándose'),('Refugio','Refugio'),('Terreno','Terreno')])
    resolucion_0 = SelectField('Resolución 058', validators = [DataRequired()], choices = [('Resolución 058',0),('Comité académico','Comité académico'),('Comité de cultura','Comité de cultura'),('Comité de seguridad y defensa integral','Comité de seguridad y defensa integral'),('Comité de comunicación e información','Comité de comunicación e información'),('Comité de madres y padres','Comité de madres y padres'),('Comité de deporte y educación física','Comité de deporte y educación física'),('Comité de contraloría social','Comité de contraloría social'),('Comité de infraestructura y hábitat','Comité de infraestructura y hábitat')])    
    submit = SubmitField('Registrar Representante')
