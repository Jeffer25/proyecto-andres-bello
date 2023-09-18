"""empty message

Revision ID: acfe2878bae7
Revises: bf114538eaea
Create Date: 2023-03-05 12:33:33.819741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acfe2878bae7'
down_revision = 'bf114538eaea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('imparte',
    sa.Column('cod_imparte', sa.Integer(), nullable=False),
    sa.Column('cod_materia', sa.String(length=10), nullable=False),
    sa.Column('cod_grado_seccion', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cod_grado_seccion'], ['grado_seccion.cod_grado_seccion'], ),
    sa.ForeignKeyConstraint(['cod_materia'], ['materia.cod_materia'], ),
    sa.PrimaryKeyConstraint('cod_imparte', 'cod_materia', 'cod_grado_seccion')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('imparte')
    # ### end Alembic commands ###
