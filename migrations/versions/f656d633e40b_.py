"""empty message

Revision ID: f656d633e40b
Revises: 4cdfad919762
Create Date: 2024-04-08 04:21:27.613561

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f656d633e40b'
down_revision: Union[str, None] = '4cdfad919762'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('refinedstatistics', sa.Column('current_ratio', sa.Numeric(precision=30, scale=10), nullable=False))
    op.add_column('refinedstatistics', sa.Column('quick_ratio', sa.Numeric(precision=30, scale=10), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('refinedstatistics', 'quick_ratio')
    op.drop_column('refinedstatistics', 'current_ratio')
    # ### end Alembic commands ###
