"""add relation between timerange and events

Revision ID: 9434ce31b95c
Revises: 26171a59dec9
Create Date: 2020-06-18 17:41:07.470107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9434ce31b95c'
down_revision = '26171a59dec9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'timerange', 'events', ['event_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'timerange', type_='foreignkey')
    # ### end Alembic commands ###
