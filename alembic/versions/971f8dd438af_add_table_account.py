"""add table account

Revision ID: 971f8dd438af
Revises: 54ad16515ad0
Create Date: 2024-11-17 15:03:17.555211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '971f8dd438af'
down_revision: Union[str, None] = '54ad16515ad0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('account', sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('email', sa.String(30)))


def downgrade() -> None:
    op.drop_table('account')
