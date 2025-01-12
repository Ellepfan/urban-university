from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    content: str
    priority: int
    slug: str
    user_id: int


class CreateTask(TaskBase):
    pass

class Task(TaskBase):
    id: int


class Config:
    orm_mode = True  # Позволяет работать с данными ORM
