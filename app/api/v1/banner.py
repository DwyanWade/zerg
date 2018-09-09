"""
Created on 2018/8/25 0:37

"""
from flask import jsonify

from app.libs.error_code import NotFound
from app.libs.redprint import RedPrint
from app.models.banner_item import BannerItem
from app.models.image import Image

__Author__ = '阿强'

api = RedPrint('banner')


@api.route('/<int:id>', methods=['GET'])
def get_item(id):
    banner_list = BannerItem.query.filter_by(banner_id=id).all()
    if banner_list:
        res_banner = []
        for banner in banner_list:
            image = Image.query.filter_by(id=banner.img_id).first()
            banner.img = image
            res_banner.append(banner.hide('banner_id', 'id', 'img_id').append('img'))
        return jsonify(res_banner)
    else:
        raise NotFound()
