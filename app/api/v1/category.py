"""
Created on 2018/8/29 21:54

"""
import operator

from flask import jsonify

from app.libs.error_code import NotFound
from app.libs.redprint import RedPrint
from app.models.category import Category
from app.models.image import Image

__Author__ = '阿强'

api = RedPrint('category')


@api.route('/all', methods=['GET'])
def get_category():
    category_list = Category.query.order_by(Category.topic_img_id).all()
    if category_list:
        img_ids = [category.topic_img_id for category in category_list]
        images = Image.query.filter(Image.id.in_(img_ids)).all()
        category_list = [category.append('img') for category in category_list]
        for i in range(0, len(images)):
            category_list[i].img = images[i]
        category_list = sorted(category_list, key=operator.itemgetter('id'))
        return jsonify(category_list)
    else:
        raise NotFound()
