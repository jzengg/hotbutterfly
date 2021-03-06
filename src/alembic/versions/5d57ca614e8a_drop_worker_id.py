"""drop worker id

Revision ID: 5d57ca614e8a
Revises: a730fc210d6c
Create Date: 2022-02-13 03:50:01.727351

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5d57ca614e8a'
down_revision = 'a730fc210d6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_session_frauds_worker_id', table_name='session_frauds')
    op.drop_column('session_frauds', 'worker_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('session_frauds', sa.Column('worker_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_index('ix_session_frauds_worker_id', 'session_frauds', ['worker_id'], unique=False)
    # ### end Alembic commands ###
