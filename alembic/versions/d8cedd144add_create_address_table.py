"""create Address table

Revision ID: d8cedd144add
Revises: 
Create Date: 2022-05-13 12:38:31.131112

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = 'd8cedd144add'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Address',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('address', sa.String(500), nullable=False),
        sa.Column('latitude', sa.Float, nullable=False),
        sa.Column('longitude', sa.Float, nullable=False),
        sa.Column('created_at', sa.DateTime, default=func.now()),
        sa.Column('updated_at', sa.DateTime, onupdate=func.now())
    )


def downgrade():
    pass
