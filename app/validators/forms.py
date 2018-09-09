"""
Created on 2018/6/6 23:04

"""
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Regexp

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ParameterException
from app.validators.base import BaseForm as Form

__Author__ = '阿强'


class ClientForm(Form):
    code = StringField(validators=[DataRequired(message='不允许为空'), length(min=5, max=60)])
    secret = StringField()

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class BannerIdForm(Form):
    id = IntegerField(validators=[DataRequired()])


class CountForm(Form):
    count = IntegerField(default=15)

    @staticmethod
    def filter_not_digit(count):
        if isinstance(count, int):
            return count
        else:
            if count.isdigit():
                return count
            else:
                raise ParameterException()


class CategoryIdForm(Form):
    id = IntegerField()


class TokenForm(Form):
    token = StringField(validators=[DataRequired()])


class AddressForm(Form):
    name = StringField(validators=[DataRequired(message='姓名不可以为空'), length(min=1, max=20)])
    mobile = StringField(validators=[DataRequired(), Regexp('^1[0-9]{10}$')])
    province = StringField(validators=[DataRequired(message='省不可以为空'), length(min=1, max=20)])
    city = StringField(validators=[DataRequired(message='城市不可以为空'), length(min=1, max=20)])
    country = StringField(validators=[length(max=20)])
    detail = StringField(validators=[DataRequired(message='详细地址填写不符合规则'),
                                     length(min=4, max=150)])


class OrderForm(Form):
    products = StringField(validators=[DataRequired()])

    @staticmethod
    def check_products(products):
        if not isinstance(products, list):
            raise ParameterException(msg='products必须是list')
        for product in products:
            try:
                product_id = product['product_id']
                count = product['count']
                if not isinstance(product_id, int):
                    raise ParameterException(msg='product_id必须是整型')
                if not isinstance(count, int):
                    raise ParameterException(msg='count必须是整型')
                if count <= 0:
                    raise ParameterException(msg='count必须是正整数')
            except KeyError:
                raise ParameterException(msg='products内参数字段有误')
        return products
