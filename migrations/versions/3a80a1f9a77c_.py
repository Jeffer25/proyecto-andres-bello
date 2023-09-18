"""empty message

Revision ID: 3a80a1f9a77c
Revises: 41b1edb142fb
Create Date: 2023-02-11 14:48:01.083672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a80a1f9a77c'
down_revision = '41b1edb142fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grado_seccion',
    sa.Column('cod_grado_seccion', sa.Integer(), nullable=False),
    sa.Column('grado_seccion', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('cod_grado_seccion')
    )
    with op.batch_alter_table('estudiante', schema=None) as batch_op:
        batch_op.add_column(sa.Column('grado_seccion_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'grado_seccion', ['grado_seccion_id'], ['cod_grado_seccion'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('estudiante', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('grado_seccion_id')

    op.drop_table('grado_seccion')
    # ### end Alembic commands ###
