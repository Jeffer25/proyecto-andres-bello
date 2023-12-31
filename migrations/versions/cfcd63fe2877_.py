"""empty message

Revision ID: cfcd63fe2877
Revises: b6133673ed23
Create Date: 2023-02-11 18:57:12.889905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfcd63fe2877'
down_revision = 'b6133673ed23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('estudiante', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cod_grado_seccion', sa.Integer(), nullable=True))
        batch_op.drop_constraint('estudiante_grado_seccion_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'grado_seccion', ['cod_grado_seccion'], ['cod_grado_seccion'])
        batch_op.drop_column('grado_seccion_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('estudiante', schema=None) as batch_op:
        batch_op.add_column(sa.Column('grado_seccion_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('estudiante_grado_seccion_id_fkey', 'grado_seccion', ['grado_seccion_id'], ['cod_grado_seccion'])
        batch_op.drop_column('cod_grado_seccion')

    # ### end Alembic commands ###
