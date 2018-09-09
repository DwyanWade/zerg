"""
Created on 2018/6/9 16:31

"""
from flask import jsonify, g, current_app
from werkzeug.contrib.cache import SimpleCache
from app.libs.auth import register
from app.libs.redprint import RedPrint
from app.libs.token_auth import token_decorator
from app.validators.forms import ClientForm

__Author__ = '阿强'

api = RedPrint('token')
cache = SimpleCache()


@api.route('/user', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    code = form.code.data
    uid_token = register(code)
    token = uid_token['token']
    uid = uid_token['uid']
    # 在这里把token写入缓存
    cache.set(uid, token, timeout=current_app.config['TOKEN_EXPIRATION'])
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


@api.route('/verify', methods=['POST'])
@token_decorator
def verify_token():
    uid = g.user.uid
    token = cache.get(uid)
    if token:
        return jsonify({
            'isValid': True
        })
    else:
        return jsonify({
            'isValid': False
        })

