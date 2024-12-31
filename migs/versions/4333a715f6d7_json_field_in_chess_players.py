"""JSON field in chess_players

Revision ID: 4333a715f6d7
Revises: 39860d144e38
Create Date: 2024-12-30 22:42:23.366203

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB


# revision identifiers, used by Alembic.
revision: str = '4333a715f6d7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('chess_players', sa.Column('pets', JSONB, nullable=True))
    op.execute(
               "CREATE EXTENSION IF NOT EXISTS pg_trgm;"
    )
    op.execute(
        "CREATE INDEX in_chess_players_pets\n"
        "ON chess_players\n"
        "USING gin((pets::text) gin_trgm_ops);"
    )
    # pass


def downgrade() -> None:
    op.drop_index('in_chess_players_pets', 'chess_players')
    op.drop_column('chess_players', 'pets')
    # pass