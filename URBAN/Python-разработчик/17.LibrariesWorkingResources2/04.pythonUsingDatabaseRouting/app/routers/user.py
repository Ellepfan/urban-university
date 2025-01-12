from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from backend.db_depends import get_db
# from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from schemas.user import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update
# Функция создания slug-строки
from slugify import slugify

from models import User

router = APIRouter(prefix='/api/user', tags=['user'])


@router.get('/')
async def all_users(get_db: Annotated[Session, Depends(get_db)]):
    users = get_db.scalar(select(User).where(User.id)).all()
    return users


@router.get('/user_id')
async def user_by_id(get_db: Annotated[Session, Depends(get_db)],
                      user_id: int):
    users = get_db.scalar(select(User).where(User.id == user_id))
    if users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User was not found')
    return users


@router.post('/create')
async def create_user(get_db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    get_db.execute(insert(User).values(username=create_user.username,
                                       firstname=create_user.firstname,
                                       lastname=create_user.lastname,
                                       age=create_user.age,
                                       slug=slugify(create_user.username)))
    get_db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put('/update')
async def update_user(get_db: Annotated[Session, Depends(get_db)],
                      user_id: int,
                      update_user: UpdateUser):
    users = get_db.scalar(select(User).where(User.id == user_id))
    if users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User was not found')
    get_db.execute(update(User).where(User.id == user_id).values(username=create_user.username,
                                                                 firstname=create_user.firstname,
                                                                 lastname=create_user.lastname,
                                                                 age=create_user.age,
                                                                 slug=slugify(create_user.username)))
    get_db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User update is successful!'
    }


@router.delete('/delete')
async def delete_user(get_db: Annotated[Session, Depends(get_db)],
                      user_id: int,
                      update_user: UpdateUser):
    users = get_db.scalar(select(User).where(User.id == user_id))
    if users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User was not found')
    get_db.execute(update(User).where(User.id == user_id).values(is_active=False))
    get_db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User update is successful!'
    }