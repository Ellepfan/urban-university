"""Add description to products

Revision ID: 04625c10ad4b
Revises: 78974c1a1760
Create Date: 2025-01-13 00:41:37.254939

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04625c10ad4b'
down_revision: Union[str, None] = '78974c1a1760'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('firstname', sa.String(), nullable=True),
    sa.Column('lastname', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('slug', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_age'), 'users', ['age'], unique=True)
    op.create_index(op.f('ix_users_firstname'), 'users', ['firstname'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_lastname'), 'users', ['lastname'], unique=True)
    op.create_index(op.f('ix_users_slug'), 'users', ['slug'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.drop_index('ix_user_id', table_name='user')
    op.drop_index('ix_user_slug', table_name='user')
    op.drop_table('user')
    op.create_index(op.f('ix_tasks_completed'), 'tasks', ['completed'], unique=False)
    op.create_index(op.f('ix_tasks_content'), 'tasks', ['content'], unique=False)
    op.create_index(op.f('ix_tasks_priority'), 'tasks', ['priority'], unique=False)
    op.create_index(op.f('ix_tasks_title'), 'tasks', ['title'], unique=False)
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.create_foreign_key(None, 'tasks', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.create_foreign_key(None, 'tasks', 'user', ['user_id'], ['id'])
    op.drop_index(op.f('ix_tasks_title'), table_name='tasks')
    op.drop_index(op.f('ix_tasks_priority'), table_name='tasks')
    op.drop_index(op.f('ix_tasks_content'), table_name='tasks')
    op.drop_index(op.f('ix_tasks_completed'), table_name='tasks')
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(), nullable=True),
    sa.Column('firstname', sa.VARCHAR(), nullable=True),
    sa.Column('lastname', sa.VARCHAR(), nullable=True),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.Column('slug', sa.VARCHAR(), nullable=True),
    sa.Column('parent_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_user_slug', 'user', ['slug'], unique=1)
    op.create_index('ix_user_id', 'user', ['id'], unique=False)
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_slug'), table_name='users')
    op.drop_index(op.f('ix_users_lastname'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_firstname'), table_name='users')
    op.drop_index(op.f('ix_users_age'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
