"""create eventplayers

Revision ID: 4e9b9a49141b
Revises: 7d2fd032a113
Create Date: 2020-06-23 00:31:01.822538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e9b9a49141b'
down_revision = '7d2fd032a113'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event_players',
    sa.Column('event_player_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.event_id'], ),
    sa.ForeignKeyConstraint(['player_id'], ['players.player_id'], ),
    sa.PrimaryKeyConstraint('event_player_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event_players')
    # ### end Alembic commands ###