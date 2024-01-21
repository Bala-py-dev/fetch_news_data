"""news_tbl

Revision ID: 89e3712afa75
Revises: b5316c712fae
Create Date: 2024-01-21 23:47:00.027309

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '89e3712afa75'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'news_tbl',
        sa.Column('id', sa.Integer(), primary_key=True, index=True, autoincrement=True),
        sa.Column('source_id', sa.String()),
        sa.Column('source_name', sa.String()),
        sa.Column('author', sa.String()),
        sa.Column('title', sa.String()),
        sa.Column('description', sa.String()),
        sa.Column('url', sa.String()),
        sa.Column('url_to_image', sa.String()),
        sa.Column('published_at', sa.DateTime()),
        sa.Column('content', sa.String()),
        sa.Column('created_at', sa.DateTime()),
    )


def downgrade() -> None:
    op.drop_table('news_tbl')
