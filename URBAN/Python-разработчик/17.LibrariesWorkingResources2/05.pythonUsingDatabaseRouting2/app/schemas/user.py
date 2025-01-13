from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int
    slug: str


class CreateUser(UserBase):
    pass

class User(UserBase):
    id: int


class Config:
    orm_mode = True  # Позволяет работать с данными ORM
