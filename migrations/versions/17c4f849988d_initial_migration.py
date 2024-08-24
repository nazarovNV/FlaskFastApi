"""Initial migration.

Revision ID: 17c4f849988d
Revises: 3740d1bad27a
Create Date: 2024-08-24 14:22:01.269054

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '17c4f849988d'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Auto-generated code; you can adjust as necessary
    op.create_table('user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(length=80), nullable=False),
        sa.Column('email', sa.String(length=120), nullable=False),
        sa.Column('password_hash', sa.String(length=128), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username'),
        sa.UniqueConstraint('email')
    )
    op.create_table('product',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=80), nullable=False),
        sa.Column('description', sa.String(length=200), nullable=True),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_product_user'),  # Указать имя ограничения
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )

def downgrade():
    # Auto-generated code; you can adjust as necessary
    op.drop_table('product')
    op.drop_table('user')


    # ### end Alembic commands ###
