#!/usr/bin/python3
"""python file that contains the class definition of a
city and an instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from relationship_state import Base, State


class City(Base):
        """ class definition of a Cities table"""
        __tablename__ = 'cities'
        id = Column(Integer, primary_key=True, nullable=False, unique=True)
        name = Column(String(128), nullable=False)
        state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
