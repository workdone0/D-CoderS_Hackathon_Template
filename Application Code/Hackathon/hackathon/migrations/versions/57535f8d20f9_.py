"""empty message

Revision ID: 57535f8d20f9
Revises: 15c0fa797121
Create Date: 2020-02-09 12:59:03.964434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57535f8d20f9'
down_revision = '15c0fa797121'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_name', sa.Text(), nullable=True),
    sa.Column('organiser_name', sa.Text(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    # ### end Alembic commands ###
