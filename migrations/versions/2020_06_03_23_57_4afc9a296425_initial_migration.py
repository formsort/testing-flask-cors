"""initial migration

Revision ID: 4afc9a296425
Revises: 
Create Date: 2020-06-03 23:57:54.075450

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4afc9a296425'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('password_hash', sa.Unicode(), nullable=True),
    sa.Column('email', sa.Unicode(), nullable=False),
    sa.Column('first_name', sa.Unicode(), nullable=False),
    sa.Column('last_name', sa.Unicode(), nullable=False),
    sa.Column('registered_at', sa.DateTime(timezone=True), server_default=sa.text('statement_timestamp()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_account_id'), 'account', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_account_id'), table_name='account')
    op.drop_table('account')
    # ### end Alembic commands ###


def upgrade_two():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('extraction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('sensor_data', postgresql.JSONB(none_as_null=True, astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_extraction_account_id'), 'extraction', ['account_id'], unique=False)
    op.create_index(op.f('ix_extraction_id'), 'extraction', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade_two():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_extraction_id'), table_name='extraction')
    op.drop_index(op.f('ix_extraction_account_id'), table_name='extraction')
    op.drop_table('extraction')
    # ### end Alembic commands ###

