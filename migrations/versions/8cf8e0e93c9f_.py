"""empty message

Revision ID: 8cf8e0e93c9f
Revises: 9b39f48193d9
Create Date: 2023-03-04 19:43:25.528039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8cf8e0e93c9f'
down_revision = '9b39f48193d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('materia', schema=None) as batch_op:
        batch_op.alter_column('cod_materia',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=10),
               existing_nullable=False,
               existing_server_default=sa.text("nextval('materia_cod_materia_seq'::regclass)"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('materia', schema=None) as batch_op:
        batch_op.alter_column('cod_materia',
               existing_type=sa.String(length=10),
               type_=sa.INTEGER(),
               existing_nullable=False,
               existing_server_default=sa.text("nextval('materia_cod_materia_seq'::regclass)"))

    # ### end Alembic commands ###
