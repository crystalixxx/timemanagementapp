"""empty message

Revision ID: d65be60b4b6c
Revises: be51b2310d3c
Create Date: 2024-07-23 13:36:19.829424

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'd65be60b4b6c'
down_revision: Union[str, None] = 'be51b2310d3c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_column('color')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('color', sa.VARCHAR(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
