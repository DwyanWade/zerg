"""
Created on 2018/8/31 21:05

"""
from sqlalchemy import Column, Integer, String

from app.models.base import Base, db

__Author__ = '阿强'


class UserAddress(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    mobile = Column(String(20), nullable=False)
    province = Column(String(20))
    city = Column(String(20))
    country = Column(String(20))
    detail = Column(String(100))
    user_id = Column(Integer, nullable=False)
    fields = ['name', 'mobile', 'province', 'city', 'country', 'detail']

    @staticmethod
    def update_user_address(uid, form):
        name = form.name.data
        mobile = form.mobile.data
        province = form.province.data
        city = form.city.data
        country = form.country.data
        detail = form.detail.data
        user_address = UserAddress.query.filter_by(user_id=uid).first()
        if user_address:
            with db.auto_commit():
                user_address.name = name
                user_address.mobile = mobile
                user_address.province = province
                user_address.city = city
                user_address.country = country
                user_address.detail = detail
        else:
            with db.auto_commit():
                user_address = UserAddress()
                user_address.user_id = uid
                user_address.name = name
                user_address.mobile = mobile
                user_address.province = province
                user_address.city = city
                user_address.country = country
                user_address.detail = detail
                db.session.add(user_address)

    @staticmethod
    def get_user_address(uid):
        user_address = UserAddress.query.filter_by(user_id=uid).first_or_404()
        return user_address

    @staticmethod
    def json_address(address):
        return {
            'id': address.id,
            'name': address.name,
            'mobile': address.mobile,
            'province': address.province,
            'city': address.city,
            'country': address.country,
            'detail': address.detail,
            'user_id': address.user_id
        }

