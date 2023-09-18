"""empty message

Revision ID: c9224fc640de
Revises: 186e43e6cd8c
Create Date: 2023-03-04 20:10:33.347356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9224fc640de'
down_revision = '186e43e6cd8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('materia',
    sa.Column('cod_materia', sa.String(length=10), nullable=False),
    sa.Column('nom_materia', sa.String(length=50), nullable=False),
    sa.Column('cedula_prof', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cedula_prof'], ['profesor.cedula_prof'], ),
    sa.PrimaryKeyConstraint('cod_materia')
    )
    with op.batch_alter_table('cursa', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'materia', ['cod_materia'], ['cod_materia'])

    with op.batch_alter_table('nota', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'materia', ['cod_materia'], ['cod_materia'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('nota', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('cursa', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    op.drop_table('materia')
    # ### end Alembic commands ###