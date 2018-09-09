"""
Created on 2018/8/27 0:22

"""
from flask import current_app
from sqlalchemy import Column, Integer, String, SmallInteger

from app.models.base import Base

__Author__ = '阿强'


class Image(Base):
    id = Column(Integer, primary_key=True)
    _url = Column('url', String(255))
    belong = Column(SmallInteger, nullable=False, default=1)
    fields = ['url']

    @property
    def url(self):
        return current_app.config['IMG_ROOT_URL'] + self._url
