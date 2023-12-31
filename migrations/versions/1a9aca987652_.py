"""empty message

Revision ID: 1a9aca987652
Revises: 207a1a473800
Create Date: 2023-02-21 20:10:58.588601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a9aca987652'
down_revision = '207a1a473800'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profesor',
    sa.Column('cedula_prof', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('apellido', sa.String(length=50), nullable=False),
    sa.Column('materiaImparte', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('cedula_prof')
    )
    op.create_table('materia',
    sa.Column('cod_materia', sa.Integer(), nullable=False),
    sa.Column('nom_materia', sa.String(length=50), nullable=False),
    sa.Column('cedula_prof', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cedula_prof'], ['profesor.cedula_prof'], ),
    sa.PrimaryKeyConstraint('cod_materia')
    )
    with op.batch_alter_table('asigna', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cedula_prof', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'profesor', ['cedula_prof'], ['cedula_prof'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('asigna', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('cedula_prof')

    op.drop_table('materia')
    op.drop_table('profesor')
    # ### end Alembic commands ###
