"""empty message

Revision ID: ea819d82982b
Revises: bbfff7ae385d
Create Date: 2023-09-18 18:58:45.845871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea819d82982b'
down_revision = 'bbfff7ae385d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grado_seccion',
    sa.Column('cod_grado_seccion', sa.Integer(), nullable=False),
    sa.Column('grado_seccion', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('cod_grado_seccion')
    )
    with op.batch_alter_table('asigna', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'grado_seccion', ['cod_grado_seccion'], ['cod_grado_seccion'])

    with op.batch_alter_table('estudiante', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'grado_seccion', ['cod_grado_seccion'], ['cod_grado_seccion'])

    with op.batch_alter_table('imparte', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'grado_seccion', ['cod_grado_seccion'], ['cod_grado_seccion'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('imparte', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('estudiante', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('asigna', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    op.drop_table('grado_seccion')
    # ### end Alembic commands ###
