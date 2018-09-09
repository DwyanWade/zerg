"""
Created on 2018/8/25 1:51

"""
from sqlalchemy import Column, Integer, String

from app.models.base import Base

__Author__ = '阿强'


class Banner(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), unique=True, nullable=False)
