from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.models import user


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String,  index=True)
    priority = Column(Integer, index=True, default=0)
    completed = Column(Boolean, index=True, default=False)
    slug = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=False)

    user = relationship('User', back_populates='tasks')


from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))