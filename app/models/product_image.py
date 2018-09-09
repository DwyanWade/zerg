"""
Created on 2018/8/30 23:53

"""
from sqlalchemy import Column, Integer

from app.models.base import Base

__Author__ = '阿强'


class ProductImage(Base):
    id = Column(Integer, primary_key=True)
    img_id = Column(Integer, nullable=False)
    order = Column(Integer, nullable=False, default=0)
    product_id = Column(Integer)