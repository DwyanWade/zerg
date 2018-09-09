"""
Created on 2018/8/28 22:40

"""
from flask import jsonify

from app.libs.redprint import RedPrint
from app.models.image import Image
from app.models.product import Product
from app.models.product_image import ProductImage
from app.models.product_property import ProductProperty
from app.validators.forms import CountForm, CategoryIdForm

__Author__ = '阿强'

api = RedPrint('product')


@api.route('/recent', methods=['GET'])
def recent_product():
    form = CountForm().validate_for_api()
    count = form.count.data
    count = CountForm.filter_not_digit(count)
    products = Product.query.limit(count).all()
    return jsonify(products)


@api.route('/by_category', methods=['GET'])
def category_product():
    form = CategoryIdForm().validate_for_api()
    id = form.id.data
    products = Product.query.filter_by(category_id=id).all()
    return jsonify(products)


@api.route('/<int:id>', methods=['GET'])
def get_detail(id):
    product = Product.query.filter_by(id=id).first_or_404()
    imagegs = ProductImage.query.filter_by(product_id=id).all()
    product_properties = ProductProperty.query.filter_by(product_id=id).all()
    imgs = []
    if imagegs:
        for img in imagegs:
            image = Image.query.filter_by(id=img.img_id).first_or_404()
            imgs.append(image)
    product.imgs = imgs
    product.properties = product_properties
    return jsonify(product.append('imgs', 'properties'))
