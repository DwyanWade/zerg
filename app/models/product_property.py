"""
Created on 2018/8/30 23:59

"""
from sqlalchemy import Column, Integer, String

from app.models.base import Base

__Author__ = '阿强'


class ProductProperty(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    detail = Column(String(255))
    product_id = Column(Integer, nullable=False)
    fields = ['name', 'detail']