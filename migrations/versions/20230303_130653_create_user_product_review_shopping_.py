"""create user, product, review, shopping_cart, whish_list, images tables

Revision ID: 85c9718a8177
Revises:
Create Date: 2023-03-03 13:06:53.685180

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# revision identifiers, used by Alembic.
revision = '85c9718a8177'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(
                        length=50), nullable=False),
                    sa.Column('name', sa.String(length=50), nullable=False),
                    sa.Column('email', sa.String(length=255), nullable=False),
                    sa.Column('hashed_password', sa.String(
                        length=255), nullable=False),
                    sa.Column('street_address', sa.String(
                        length=100), nullable=False),
                    sa.Column('city', sa.String(length=50), nullable=False),
                    sa.Column('state', sa.String(length=10), nullable=False),
                    sa.Column('zip_code', sa.Integer(), nullable=False),
                    sa.Column('profile_img', sa.String(
                        length=500), nullable=True),
                    sa.Column('created_date', sa.DateTime(timezone=True),
                              server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('username')
                    )
    op.create_table('products',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(length=160), nullable=False),
                    sa.Column('price', sa.Integer(), nullable=False),
                    sa.Column('description', sa.String(
                        length=1000), nullable=False),
                    sa.Column('category', sa.String(
                        length=70), nullable=False),
                    sa.Column('brand', sa.String(length=70), nullable=False),
                    sa.Column('image', sa.String(length=500), nullable=False),
                    sa.Column('quantity', sa.Integer(), nullable=True),
                    sa.Column('owner_id', sa.Integer(), nullable=False),
                    sa.Column('created_date', sa.DateTime(timezone=True),
                              server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
                    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('shopping_carts',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('total', sa.Integer(), nullable=True),
                    sa.Column('checked_out', sa.Boolean(), nullable=False),
                    sa.Column('estimated_delivery',
                              sa.String(), nullable=True),
                    sa.Column('owner_id', sa.Integer(), nullable=False),
                    sa.Column('order_placed', sa.String(), nullable=True),
                    sa.Column('created_date', sa.DateTime(timezone=True),
                              server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
                    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('wish_lists',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=50), nullable=False),
                    sa.Column('owner_id', sa.Integer(), nullable=False),
                    sa.Column('created_date', sa.DateTime(timezone=True),
                              server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
                    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('product_carts',
                    sa.Column('products', sa.Integer(), nullable=False),
                    sa.Column('shopping_carts', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['products'], ['products.id'], ),
                    sa.ForeignKeyConstraint(['shopping_carts'], [
                                            'shopping_carts.id'], ),
                    sa.PrimaryKeyConstraint('products', 'shopping_carts')
                    )
    op.create_table('product_lists',
                    sa.Column('products', sa.Integer(), nullable=False),
                    sa.Column('wish_lists', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['products'], ['products.id'], ),
                    sa.ForeignKeyConstraint(
                        ['wish_lists'], ['wish_lists.id'], ),
                    sa.PrimaryKeyConstraint('products', 'wish_lists')
                    )
    op.create_table('reviews',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(length=50), nullable=False),
                    sa.Column('review', sa.String(length=400), nullable=False),
                    sa.Column('rating', sa.Integer(), nullable=False),
                    sa.Column('owner_id', sa.Integer(), nullable=False),
                    sa.Column('product_id', sa.Integer(), nullable=False),
                    sa.Column('created_date', sa.DateTime(timezone=True),
                              server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
                    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
                    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('images',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('url', sa.String(length=1000), nullable=True),
                    sa.Column('owner_id', sa.Integer(), nullable=False),
                    sa.Column('product_id', sa.Integer(), nullable=True),
                    sa.Column('review_id', sa.Integer(), nullable=True),
                    sa.Column('created_date', sa.DateTime(timezone=True),
                              server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
                    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
                    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
                    sa.ForeignKeyConstraint(['review_id'], ['reviews.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )

    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE products SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE shopping_carts SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE wish_lists SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE product_carts SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE product_lists SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE reviews SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE images SET SCHEMA {SCHEMA};")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('images')
    op.drop_table('reviews')
    op.drop_table('product_lists')
    op.drop_table('product_carts')
    op.drop_table('wish_lists')
    op.drop_table('shopping_carts')
    op.drop_table('products')
    op.drop_table('users')
    # ### end Alembic commands ###
