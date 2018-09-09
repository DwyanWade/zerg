"""
Created on 2018/8/25 1:22

"""
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base

__Author__ = '阿强'


class BannerItem(Base):
    id = Column(Integer, primary_key=True)
    img_id = Column(Integer)
    key_word = Column(Integer)
    type = Column(Integer)
    banner_id = Column(Integer)
    fields = ['id', 'img_id', 'key_word', 'type', 'banner_id']
