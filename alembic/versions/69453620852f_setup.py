"""setup

Revision ID: 69453620852f
Revises: 
Create Date: 2023-04-15 15:22:37.144686

"""
import uuid
from datetime import datetime

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from passlib.context import CryptContext

# revision identifiers, used by Alembic.
revision = '69453620852f'
down_revision = None
branch_labels = None
depends_on = None



def upgrade():
    pwd_crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")
    #Users table
    user = op.create_table(
        'user',
        sa.Column('id', UUID(), autoincrement=False, nullable=False),
        sa.Column('email', sa.String(255), unique=True, nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('firstname', sa.String(255), nullable=False),
        sa.Column('lastname', sa.String(255), nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False, index=True),
        sa.Column('updated_at', sa.DateTime, nullable=False, index=True),
        sa.PrimaryKeyConstraint('id'),
    )

    #brands table
    brand = op.create_table(
        'brand',
        sa.Column('id', UUID(), autoincrement=False, nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, index=True),
        sa.Column('updated_at', sa.DateTime, nullable=False, index=True),
        sa.PrimaryKeyConstraint('id'),
    )

    #product table
    op.create_table(
        'product',
        sa.Column('id', UUID(), autoincrement=False, nullable=False),
        sa.Column('sku', sa.String(255), unique=True, nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', sa.String(255), nullable=False),
        sa.Column('stock', sa.Integer, nullable=False, default=0),
        sa.Column('price', sa.DECIMAL(10, 2), nullable=False),
        sa.Column('status', sa.Boolean, nullable=False),
        sa.Column('brand_id', UUID(), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, index=True),
        sa.Column('updated_at', sa.DateTime, nullable=False, index=True),
        sa.ForeignKeyConstraint(['brand_id'], ['brand.id'],),
        sa.PrimaryKeyConstraint('id'),
    )

    #product querying table
    op.create_table(
        'product_consult',
        sa.Column('id', UUID(), autoincrement=False, nullable=False),
        sa.Column('product_id', UUID(), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, index=True),
        sa.Column('updated_at', sa.DateTime, nullable=False, index=True),
        sa.ForeignKeyConstraint(['product_id'], ['product.id'],),
        sa.PrimaryKeyConstraint('id'),
    )

    super_admin_pwd = pwd_crypt.hash("superadmin")

    #Seeding table of user with admin user
    op.bulk_insert(user,
    [
        {'id': str(uuid.uuid4()), 'email':'danielavilla2898@gmail.com', 'password': super_admin_pwd,
         'firstname': 'Daniela', 'lastname': 'Villa', 'created_at': datetime.now(), 'updated_at': datetime.now()},
        {'id': str(uuid.uuid4()), 'email':'fasttest2023api@outlook.com', 'password': super_admin_pwd,
         'firstname': 'John', 'lastname': 'Smith',  'created_at': datetime.now(), 'updated_at': datetime.now()},
    ])

    #Seeding brand table

    op.bulk_insert(brand,
    [
        {'id': str(uuid.uuid4()), 'name':'luuna', 'description': 'Luuna',
         'created_at': datetime.now(), 'updated_at': datetime.now()},
        {'id': str(uuid.uuid4()), 'name':'nooz', 'description': 'Nooz',
         'created_at': datetime.now(), 'updated_at': datetime.now()},
        {'id': str(uuid.uuid4()), 'name':'mappa', 'description': 'Mappa',
         'created_at': datetime.now(), 'updated_at': datetime.now()},
        {'id': str(uuid.uuid4()), 'name':'ergo', 'description': 'Ergo',
         'created_at': datetime.now(), 'updated_at': datetime.now()},
        {'id': str(uuid.uuid4()), 'name':'nubed', 'description': 'Nubed',
         'created_at': datetime.now(), 'updated_at': datetime.now()},
    ])

def downgrade():
    op.drop_table('user')
    op.drop_table('brand')
    op.drop_table('product')
    op.drop_table('product_consult')
    
