"""empty message

Revision ID: 08bf07e4b63d
Revises: 
Create Date: 2024-02-14 17:23:22.084799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08bf07e4b63d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('checked', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo')
    # ### end Alembic commands ###
