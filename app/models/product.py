from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func
from product_shopping_cart import product_shopping_cart
from product_wish_list import product_wish_list


class Product(db.Model):
    __tablename__ = 'products'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(600), nullable=False)
    category = db.Column(db.String(40), nullable=False)
    brand = db.Column(db.String(40), nullable=False)
    image = db.Column(db.String(400), nullable=False)
    count = db.Column(db.Integer, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    created_date = db.Column(db.DateTime(timezone=True), server_default=func.now())


    # ! Relationships
    products_owned = db.relationship("User", back_populates="owned_products")
    product_reviews = db.relationship("Review", back_populates="reviews_product")
    product_carts = db.relationship("ShoppingCart", secondary=product_shopping_cart, back_populates="carts_product")
    product_lists = db.relationship("WishList", secondary=product_wish_list, back_populates="lists_product")
    product_images = db.relationship("Product", back_populates="images_product", cascade="all,delete")

    # ? Methods
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'description': self.description,
            'category': self.category,
            'brand': self.brand,
            'image': self.image,
            'count': self.count,
            'ownerId': self.owner_id,
            'productImages': [image.to_dict()['id'] for image in self.product_images]
        }

    def to_dict_basic(self):
        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'description': self.description,
            'category': self.category,
            'brand': self.brand,
            'image': self.image,
            # 'count': self.count,
            'ownerId': self.owner_id,
        }
