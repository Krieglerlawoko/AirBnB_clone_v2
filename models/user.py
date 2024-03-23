#!/usr/bin/python3
"""User class defined"""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """user for a MySQL database represented"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
