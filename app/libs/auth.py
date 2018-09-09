"""
Created on 2018/8/30 0:31

"""
from flask import current_app, json
from urllib import request as _request

from app.libs.error_code import ServerError
from app.models.user import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
__Author__ = '阿强'


def register(code):
    appid = current_app.config['WX_APPID']
    app_secret = current_app.config['APP_SECRET']
    login_url = current_app.config['LOGIN_URL'].format(appid, app_secret, code)
    uid_token = __http_to_wx(login_url)
    return uid_token


def __http_to_wx(url):
    res = _request.Request(url=url)
    res = _request.urlopen(res)
    res = res.read().decode('ascii')
    res = json.loads(res)
    if 'openid' in res.keys():
        uid = User.register(res['openid'])
        uid_token = generate_auth_token(uid)
        return uid_token
    else:
        raise ServerError(msg='获取openid时异，微信内部错误')


def generate_auth_token(uid, scope=None):
    """生成令牌"""
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=current_app.config['TOKEN_EXPIRATION'])
    token = s.dumps({
        'uid': uid,
        'scope': scope
    })
    return {
        'uid': uid,
        'token': token
    }