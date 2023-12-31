"""empty message

Revision ID: b6133673ed23
Revises: 3a80a1f9a77c
Create Date: 2023-02-11 16:53:09.601369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6133673ed23'
down_revision = '3a80a1f9a77c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('estudiante', schema=None) as batch_op:
        batch_op.drop_column('curso')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('estudiante', schema=None) as batch_op:
        batch_op.add_column(sa.Column('curso', sa.VARCHAR(length=30), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
