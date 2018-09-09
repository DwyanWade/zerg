"""
Created on 2018/8/3 0:12

"""
from sqlalchemy import Column, Integer, String

from app.models.base import Base

__Author__ = '阿强'


class Category(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    topic_img_id = Column(Integer)
    description = Column(String(100))
    fields = ['id', 'name', 'topic_img_id']