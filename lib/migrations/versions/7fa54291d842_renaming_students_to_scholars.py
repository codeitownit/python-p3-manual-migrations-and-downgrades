"""Renaming students to scholars

Revision ID: 7fa54291d842
Revises: 791279dd0760
Create Date: 2023-12-10 12:06:59.545728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fa54291d842'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
