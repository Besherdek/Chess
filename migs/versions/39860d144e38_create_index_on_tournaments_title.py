"""Create index on tournaments title

Revision ID: 39860d144e38
Revises: 8b295d3319ff
Create Date: 2024-12-30 16:33:29.759989

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39860d144e38'
down_revision: Union[str, None] = '8b295d3319ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index('in_tournaments_title', 'tournaments', ['title'],  if_not_exists=True)


def downgrade() -> None:
    op.drop_index('in_tournaments_title', 'tournaments')