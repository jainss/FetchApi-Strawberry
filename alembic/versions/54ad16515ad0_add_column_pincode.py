"""add column pincode

Revision ID: 54ad16515ad0
Revises: 
Create Date: 2024-11-17 14:55:33.597945

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54ad16515ad0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('pincode', sa.String(30)))


def downgrade() -> None:
    op.drop_column('users', 'pincode')
