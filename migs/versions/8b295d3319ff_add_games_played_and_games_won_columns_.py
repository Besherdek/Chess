"""Add games_played and games_won columns to chess_players table

Revision ID: 8b295d3319ff
Revises: 3fdc4966974d
Create Date: 2024-12-30 16:29:37.548137

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b295d3319ff'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('chess_players', sa.Column('games_played', sa.Integer, nullable=False, server_default='0'))
    op.add_column('chess_players', sa.Column('games_won', sa.Integer, nullable=False, server_default='0'))
    op.create_check_constraint('positive_games_played', 'chess_players', 'games_played >= 0')
    op.create_check_constraint('positive_games_won', 'chess_players', 'games_won >= 0')
    op.create_check_constraint('played_more_than_won', 'chess_players', 'games_won <= games_played')


def downgrade() -> None:
    op.drop_constraint('positive_games_played', 'chess_players')
    op.drop_constraint('positive_games_won', 'chess_players')
    op.drop_constraint('played_more_than_won', 'chess_players')
    op.drop_column('chess_players', 'games_played')
    op.drop_column('chess_players', 'games_won')