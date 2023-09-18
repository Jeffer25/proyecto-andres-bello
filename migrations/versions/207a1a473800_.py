"""empty message

Revision ID: 207a1a473800
Revises: 0bacb28fcc75
Create Date: 2023-02-21 19:47:42.107590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '207a1a473800'
down_revision = '0bacb28fcc75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grado_seccion',
    sa.Column('cod_grado_seccion', sa.Integer(), nullable=False),
    sa.Column('grado_seccion', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('cod_grado_seccion')
    )
    op.create_table('asigna',
    sa.Column('cod_asignar', sa.Integer(), nullable=False),
    sa.Column('cedula_estudiante', sa.Integer(), nullable=False),
    sa.Column('cod_grado_seccion', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cedula_estudiante'], ['estudiante.cedula'], ),
    sa.ForeignKeyConstraint(['cod_grado_seccion'], ['grado_seccion.cod_grado_seccion'], ),
    sa.PrimaryKeyConstraint('cod_asignar', 'cedula_estudiante', 'cod_grado_seccion')
    )
    op.create_table('cursa',
    sa.Column('cod_cursa', sa.Integer(), nullable=False),
    sa.Column('cedula_estudiante', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cedula_estudiante'], ['estudiante.cedula'], ),
    sa.PrimaryKeyConstraint('cod_cursa', 'cedula_estudiante')
    )
    with op.batch_alter_table('estudiante', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cod_grado_seccion', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'grado_seccion', ['cod_grado_seccion'], ['cod_grado_seccion'])
        batch_op.drop_column('curso')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)

    with op.batch_alter_table('estudiante', schema=None) as batch_op:
        batch_op.add_column(sa.Column('curso', sa.VARCHAR(length=30), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('cod_grado_seccion')

    op.drop_table('cursa')
    op.drop_table('asigna')
    op.drop_table('grado_seccion')
    # ### end Alembic commands ###