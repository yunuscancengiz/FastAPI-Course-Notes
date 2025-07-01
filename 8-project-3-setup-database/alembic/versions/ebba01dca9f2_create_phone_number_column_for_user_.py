"""create phone number column for User table

Revision ID: ebba01dca9f2
Revises: 
Create Date: 2025-07-01 17:42:45.704664

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ebba01dca9f2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(table_name='users', column=sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column(table_name='users', column_name='phone_number')
