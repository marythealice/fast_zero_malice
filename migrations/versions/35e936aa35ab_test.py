"""test

Revision ID: 35e936aa35ab
Revises: 24b77645ba7b
Create Date: 2025-02-05 20:11:04.508380

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '35e936aa35ab'
down_revision: Union[str, None] = '24b77645ba7b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'created_at', 
                sa.DateTime(), 
                server_default=sa.text('(CURRENT_TIMESTAMP)'), 
                nullable=False)
        )

    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'updated_at', 
                sa.DateTime(), 
                server_default=sa.text('(CURRENT_TIMESTAMP)'), 
                nullable=False)
                
        )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:  
        batch_op.drop_column('updated_at')

    with op.batch_alter_table('todos', schema=None) as batch_op:  
        batch_op.drop_column('created_at')    
    # ### end Alembic commands ###
