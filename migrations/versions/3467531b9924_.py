"""empty message

Revision ID: 3467531b9924
Revises: 4b0d642aa079
Create Date: 2021-09-22 00:07:26.733518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3467531b9924'
down_revision = '4b0d642aa079'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('weight', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('height', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'height')
    op.drop_column('user', 'weight')
    # ### end Alembic commands ###
