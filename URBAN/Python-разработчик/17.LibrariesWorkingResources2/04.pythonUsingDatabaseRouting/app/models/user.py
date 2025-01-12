from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.models import *


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String,unique=True,index=True)
    firstname = Column(String,unique=True,index=True)
    lastname = Column(String,unique=True,index=True)
    age = Column(Integer,unique=True,index=True)
    slug = Column(String, unique=True, index=True)

    tasks = relationship('Task', back_populates='user')


from sqlalchemy.schema import CreateTable

print(CreateTable(User.__table__))
