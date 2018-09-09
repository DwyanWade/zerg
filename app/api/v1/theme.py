"""
Created on 2018/8/27 21:29

"""
from flask import jsonify

from app.libs.error_code import NotFound
from app.libs.redprint import RedPrint
from app.models.image import Image
from app.models.product import Product
from app.models.theme import Theme
from app.models.theme_product import ThemeProduct

__Author__ = '阿强'

api = RedPrint('theme')


@api.route('', methods=['GET'])
def get_theme():
    theme_list = Theme.query.all()
    if theme_list:
        res_theme = []
        for theme in theme_list:
            topic_image = Image.query.filter_by(id=theme.topic_img_id).first()
            head_image = Image.query.filter_by(id=theme.head_img_id).first()
            theme.topic_img = topic_image
            theme.head_img = head_image
            res_theme.append(theme.append('topic_img', 'head_img'))
        return jsonify(res_theme)
    else:
        raise NotFound()


@api.route('/<int:id>', methods=['GET'])
def get_theme_type(id):
    theme_product = ThemeProduct.query.filter_by(theme_id=id).all()
    theme_data = Theme.query.filter_by(id=id).first()
    topic_image = Image.query.filter_by(id=theme_data.topic_img_id).first()
    head_image = Image.query.filter_by(id=theme_data.head_img_id).first()
    if theme_product:
        res_product = []
        for key in theme_product:
            product = Product.query.filter_by(id=key.product_id).first()
            res_product.append(product)
        theme_data.products = res_product
        theme_data.head_img = head_image
        theme_data.topic_img = topic_image
        return jsonify(theme_data.append('products', 'topic_img', 'head_img'))
    else:
        raise NotFound()
