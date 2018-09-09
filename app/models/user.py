"""
Created on 2018/6/6 23:25

"""
from sqlalchemy import Column, Integer, String

from app.models.base import Base, db

__Author__ = '阿强'


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    openid = Column(String(50), unique=True, nullable=False)
    nickname = Column(String(50))
    extend = Column(String(255))

    @staticmethod
    def register(openid):
        user = User.query.filter_by(openid=openid).first()
        if not user:
            with db.auto_commit():
                user = User()
                user.openid = openid
                db.session.add(user)
            return user.id
        else:
            return user.id

