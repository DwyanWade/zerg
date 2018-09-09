"""
Created on 2018/9/2 1:13

"""
from flask import g, jsonify

from app.libs.redprint import RedPrint
from app.libs.token_auth import token_decorator
from app.models.order import Order
from app.models.order_product import OrderProduct
from app.models.product import Product
from app.validators.forms import OrderForm

__Author__ = '阿强'

api = RedPrint('order')


@api.route('', methods=['POST'])
@token_decorator
def place_order():
    uid = g.user.uid
    form = OrderForm().validate_for_api()
    products = form.products.data
    # 订单商品参数字段校验
    products = OrderForm.check_products(products)
    # 库存量检测
    order_info = Product.check_stock(products)
    if order_info['pass']:
        # 生成订单，写入数据库
        order_info = Order.generator_order(uid, order_info)
        res = OrderProduct.mark_order(order_info, products)
        return jsonify(res)
    else:
        return jsonify(order_info)
