"""initial

Revision ID: 26171a59dec9
Revises:
Create Date: 2020-06-18 17:36:24.431212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26171a59dec9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('players', sa.Integer(), nullable=False),
    sa.Column('time', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('token')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('token',
    sa.Column('token', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('player_id', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], name='token_player_id_fkey'),
    sa.PrimaryKeyConstraint('token', name='token_pkey'),
    sa.UniqueConstraint('player_id', name='token_player_id_key')
    )
    op.drop_table('events')
    # ### end Alembic commands ###
