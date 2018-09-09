"""
Created on 2018/9/3 22:03

"""
from sqlalchemy import Column, Integer

from app.models.base import Base, db

__Author__ = '阿强'


class OrderProduct(Base):
    order_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, primary_key=True)
    count = Column(Integer, nullable=False)
    delete_time = Column(Integer)
    update_time = Column(Integer)

    @staticmethod
    def mark_order(order_info, products):
        for product in products:
            with db.auto_commit():
                order_product = OrderProduct()
                order_product.order_id = order_info['order_id']
                order_product.product_id = product['product_id']
                order_product.count = product['count']
                db.session.add(order_product)
        return order_info
