"""empty message

Revision ID: 9b39f48193d9
Revises: fc1888b33fa4
Create Date: 2023-03-04 14:20:52.018077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b39f48193d9'
down_revision = 'fc1888b33fa4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grado_seccion',
    sa.Column('cod_grado_seccion', sa.Integer(), nullable=False),
    sa.Column('grado_seccion', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('cod_grado_seccion')
    )
    op.create_table('profesor',
    sa.Column('cedula_prof', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('apellido', sa.String(length=50), nullable=False),
    sa.Column('materiaImparte', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('cedula_prof')
    )
    op.create_table('representante',
    sa.Column('nombre', sa.String(length=60), nullable=False),
    sa.Column('apellido', sa.String(length=60), nullable=False),
    sa.Column('nacionalidad', sa.String(length=15), nullable=False),
    sa.Column('cedula', sa.Integer(), nullable=False),
    sa.Column('parentesco', sa.String(length=30), nullable=False),
    sa.Column('lugar_naci', sa.String(length=200), nullable=False),
    sa.Column('telefono', sa.BigInteger(), nullable=False),
    sa.Column('telefono_alt', sa.BigInteger(), nullable=False),
    sa.Column('profesion', sa.String(length=100), nullable=False),
    sa.Column('telefono_trab', sa.BigInteger(), nullable=False),
    sa.Column('direccion_trab', sa.String(length=200), nullable=False),
    sa.Column('vive_chacao', sa.String(length=10), nullable=False),
    sa.Column('direccion_dom', sa.String(length=200), nullable=False),
    sa.Column('estado_viv_infra', sa.String(length=100), nullable=False),
    sa.Column('estado_viv_tipo', sa.String(length=100), nullable=False),
    sa.Column('estado_viv_cond', sa.String(length=100), nullable=False),
    sa.Column('resolucion_0', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('cedula')
    )
    op.create_table('user',
    sa.Column('username', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('names', sa.String(length=50), nullable=False),
    sa.Column('lastnames', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=254), nullable=False),
    sa.Column('phone', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('username')
    )
    op.create_table('estudiante',
    sa.Column('cedula', sa.Integer(), nullable=False),
    sa.Column('responsable', sa.String(length=60), nullable=False),
    sa.Column('tipo_inscrip', sa.String(length=30), nullable=False),
    sa.Column('antecedente_escolar', sa.String(length=30), nullable=False),
    sa.Column('nombres', sa.String(length=60), nullable=False),
    sa.Column('apellidos', sa.String(length=60), nullable=False),
    sa.Column('genero', sa.String(length=15), nullable=False),
    sa.Column('nacionalidad', sa.String(length=15), nullable=False),
    sa.Column('fecha_naci', sa.Date(), nullable=False),
    sa.Column('parto', sa.String(length=200), nullable=False),
    sa.Column('edad', sa.Integer(), nullable=False),
    sa.Column('lateralidad', sa.String(length=30), nullable=False),
    sa.Column('lugar_naci', sa.String(length=200), nullable=False),
    sa.Column('peso', sa.Float(), nullable=False),
    sa.Column('estatura', sa.Float(), nullable=False),
    sa.Column('hermanos', sa.String(length=20), nullable=False),
    sa.Column('hermanos_inst', sa.String(length=20), nullable=False),
    sa.Column('talla_camisa', sa.String(length=10), nullable=False),
    sa.Column('talla_pantalon', sa.String(length=10), nullable=False),
    sa.Column('salud', sa.String(length=50), nullable=False),
    sa.Column('covid', sa.String(length=20), nullable=False),
    sa.Column('vacunas_covid', sa.String(length=50), nullable=False),
    sa.Column('atencion_espec', sa.String(length=50), nullable=False),
    sa.Column('email_estud', sa.String(length=254), nullable=False),
    sa.Column('equipo_tecn', sa.String(length=50), nullable=False),
    sa.Column('acceso_inter', sa.String(length=200), nullable=False),
    sa.Column('redes_soc', sa.String(length=200), nullable=False),
    sa.Column('canaima', sa.String(length=10), nullable=False),
    sa.Column('representante_id', sa.Integer(), nullable=True),
    sa.Column('cod_grado_seccion', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cod_grado_seccion'], ['grado_seccion.cod_grado_seccion'], ),
    sa.ForeignKeyConstraint(['representante_id'], ['representante.cedula'], ),
    sa.PrimaryKeyConstraint('cedula')
    )
    op.create_table('materia',
    sa.Column('cod_materia', sa.Integer(), nullable=False),
    sa.Column('nom_materia', sa.String(length=50), nullable=False),
    sa.Column('cedula_prof', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cedula_prof'], ['profesor.cedula_prof'], ),
    sa.PrimaryKeyConstraint('cod_materia')
    )
    op.create_table('asigna',
    sa.Column('cod_asignar', sa.Integer(), nullable=False),
    sa.Column('cedula_estudiante', sa.Integer(), nullable=False),
    sa.Column('cedula_prof', sa.Integer(), nullable=False),
    sa.Column('cod_grado_seccion', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cedula_estudiante'], ['estudiante.cedula'], ),
    sa.ForeignKeyConstraint(['cedula_prof'], ['profesor.cedula_prof'], ),
    sa.ForeignKeyConstraint(['cod_grado_seccion'], ['grado_seccion.cod_grado_seccion'], ),
    sa.PrimaryKeyConstraint('cod_asignar', 'cedula_estudiante', 'cedula_prof', 'cod_grado_seccion')
    )
    op.create_table('cursa',
    sa.Column('cod_cursa', sa.Integer(), nullable=False),
    sa.Column('cedula_estudiante', sa.Integer(), nullable=False),
    sa.Column('cod_materia', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cedula_estudiante'], ['estudiante.cedula'], ),
    sa.ForeignKeyConstraint(['cod_materia'], ['materia.cod_materia'], ),
    sa.PrimaryKeyConstraint('cod_cursa', 'cedula_estudiante', 'cod_materia')
    )
    op.create_table('nota',
    sa.Column('cod_nota', sa.Integer(), nullable=False),
    sa.Column('nota_1er_lapso', sa.Integer(), nullable=False),
    sa.Column('nota_2do_lapso', sa.Integer(), nullable=False),
    sa.Column('nota_3er_lapso', sa.Integer(), nullable=False),
    sa.Column('promedio', sa.Integer(), nullable=False),
    sa.Column('ced_estudiante', sa.Integer(), nullable=True),
    sa.Column('cod_materia', sa.Integer(), nullable=True),
    sa.Column('cedula_prof', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ced_estudiante'], ['estudiante.cedula'], ),
    sa.ForeignKeyConstraint(['cedula_prof'], ['profesor.cedula_prof'], ),
    sa.ForeignKeyConstraint(['cod_materia'], ['materia.cod_materia'], ),
    sa.PrimaryKeyConstraint('cod_nota')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nota')
    op.drop_table('cursa')
    op.drop_table('asigna')
    op.drop_table('materia')
    op.drop_table('estudiante')
    op.drop_table('user')
    op.drop_table('representante')
    op.drop_table('profesor')
    op.drop_table('grado_seccion')
    # ### end Alembic commands ###
