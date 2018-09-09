"""
Created on 2018/9/3 21:49

"""
import json

from flask import jsonify
from sqlalchemy import Column, Integer, String, Float, Text

from app.libs.helper import generator_order_no, timestamp_to_localtime
from app.models.base import Base, db
from app.models.user_address import UserAddress

__Author__ = '阿强'


class Order(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_no = Column(String(20), nullable=False)
    user_id = Column(Integer, nullable=False)
    delete_time = Column(Integer)
    total_price = Column(Float, nullable=False)
    snap_img = Column(String(255))
    snap_name = Column(String(80))
    total_count = Column(Integer(), default=0)
    update_time = Column(Integer)
    snap_items = Column(Text)
    snap_address = Column(String(500))
    prepay_id = Column(String(100))

    @staticmethod
    def generator_order(uid, order_info):
        address = UserAddress.get_user_address(uid)
        address = UserAddress.json_address(address)
        if len(order_info['pStatusArray']) > 1:
            snap_name = order_info['pStatusArray'][0]['name'] + '等'
        else:
            snap_name = order_info['pStatusArray'][0]['name']
        with db.auto_commit():
            order = Order()
            order.order_no = generator_order_no()
            order.user_id = uid
            order.total_price = order_info['orderPrice']
            order.snap_img = order_info['pStatusArray'][0]['mainImgUrl']
            order.snap_name = snap_name
            order.total_count = order_info['totalCount']
            order.snap_items = json.dumps(order_info['pStatusArray'])
            order.snap_address = json.dumps(address)
            db.session.add(order)
        create_time = timestamp_to_localtime(order.create_time)
        return {
            'pass': True,
            'order_id': order.id,
            'order_no': order.order_no,
            'create_time': create_time
        }
