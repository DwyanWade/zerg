"""
Created on 2018/8/28 0:27

"""
from sqlalchemy import Column, Integer

from app.models.base import Base

__Author__ = '阿强'


class ThemeProduct(Base):
    theme_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, primary_key=True)