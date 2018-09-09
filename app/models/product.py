"""
Created on 2018/8/28 0:29

"""
from flask import current_app
from sqlalchemy import Column, Integer, String, Float, SmallInteger

from app.models.base import Base

__Author__ = '阿强'


class Product(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    category_id = Column(Integer)
    _main_img_url = Column('main_img_url', String(255))
    belong = Column(SmallInteger, nullable=False, default=1)
    summary = Column(String(50))
    img_id = Column(Integer)
    fields = ['id', 'name', 'price', 'stock', 'main_img_url', 'summary', 'img_id']

    @property
    def main_img_url(self):
        return current_app.config['IMG_ROOT_URL'] + self._main_img_url

    @staticmethod
    def check_stock(products):
        p_status_array = []
        order_price = 0
        total_count = 0
        for item in products:
            product = Product.query.filter_by(id=item['product_id']).first_or_404()
            p_status_array.append({
                "count": item['count'],
                "haveStock": product.stock >= item['count'],
                "id": item['product_id'],
                "name": product.name,
                "totalPrice": product.price * item['count'],
                "mainImgUrl": product.main_img_url
            })
            order_price += product.price * item['count']
            total_count += item['count']
        if Product._check_stock(p_status_array):
            return {
                "pass": True,
                "orderPrice": order_price,
                "totalCount": total_count,
                "pStatusArray": p_status_array
            }
        else:
            return {
                "pass": False,
                "orderPrice": order_price,
                "order_id": -1,
                "totalCount": total_count,
                "pStatusArray": p_status_array
            }

    @staticmethod
    def _check_stock(status_array):
        res = [1 for item in status_array if item['haveStock']]
        if len(res) == len(status_array):
            return True
        else:
            return False
