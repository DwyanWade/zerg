"""
Created on 2018/8/31 21:32

"""
from flask import g, jsonify

from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.libs.token_auth import token_decorator
from app.models.user_address import UserAddress
from app.validators.forms import AddressForm

__Author__ = '阿强'

api = RedPrint('address')


@api.route('', methods=['POST'])
@token_decorator
def update_address():
    uid = g.user.uid
    form = AddressForm().validate_for_api()
    UserAddress.update_user_address(uid, form)
    return Success()


@api.route('', methods=['GET'])
@token_decorator
def get_address():
    uid = g.user.uid
    address = UserAddress.get_user_address(uid)
    return jsonify(address)
