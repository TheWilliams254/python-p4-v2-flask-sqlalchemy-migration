"""rename address

Revision ID: 24c38752afaa
Revises: f5768d6affb1
Create Date: 2025-06-15 08:39:09.019008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24c38752afaa'
down_revision = 'f5768d6affb1'
branch_labels = None
depends_on = None


def upgrade():
    # Rename 'address' to 'location' without dropping data
    op.alter_column('departments', 'address', new_column_name='location')


def downgrade():
    # Rename 'location' back to 'address'
    op.alter_column('departments', 'location', new_column_name='address')
