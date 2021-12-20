#!/usr/bin/python3
"""State class:
    inherits from Base
    links to the MySQL table states """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    ''' Empty class that inherits from Base '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
