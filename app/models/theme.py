"""
Created on 2018/8/27 21:04

"""
from sqlalchemy import Column, Integer, String

from app.models.base import Base

__Author__ = '阿强'


class Theme(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(255))
    topic_img_id = Column(Integer)
    head_img_id = Column(Integer)
    fields = ['id', 'name', 'description']