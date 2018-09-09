"""
Created on 2018/6/6 0:45

"""
from flask import Blueprint
from app.api.v1 import token, banner, theme, product, category, address, order

__Author__ = '阿强'


def create_blueprint_v1():
    bp_vi = Blueprint('v1', __name__)
    category.api.register(bp_vi)
    product.api.register(bp_vi)
    theme.api.register(bp_vi)
    banner.api.register(bp_vi)
    token.api.register(bp_vi)
    address.api.register(bp_vi)
    order.api.register(bp_vi)
    return bp_vi
