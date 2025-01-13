from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import Annotated
from app.backend.db_depends import get_db
from sqlalchemy import insert, select, update

from app.schemas.task import Task, CreateTask
from app.schemas.user import User, CreateUser
from slugify import slugify

router = APIRouter(
    prefix='/api/users',
    tags=['users']
)

DbSession = Annotated[Session, Depends(get_db)]


@router.get('/', response_model=list[User])
async def all_users(db: DbSession):
    query = text("SELECT * FROM users")
    result = db.execute(query).fetchall()
    return [User(id=row.id, username=row.username, firstname=row.firstname, lastname=row.lastname, age=row.age,
                 slug=row.slug) for row in result]


@router.get('/user_id')
async def user_by_id(user_id: int, db: DbSession):
    select_query = text("SELECT * FROM users WHERE id = :id")
    result = db.execute(select_query, {"id": user_id}).fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return User(
        id=result.id,
        username=result.username,
        firstname=result.firstname,
        lastname=result.lastname,
        age=result.age,
        slug=result.slug
    )


@router.post('/create', response_model=User)
async def create_user(user: CreateUser, db: DbSession):
    select_query = text("SELECT * FROM users WHERE username = :username")
    chek_username = db.execute(select_query, {"username": user.username}).fetchone()
    if chek_username:
        raise HTTPException(status_code=404, detail="User found")
    query = text("INSERT INTO users (username, firstname, lastname, age, slug) VALUES "
                 "(:username,"
                 ":firstname,"
                 ":lastname,"
                 ":age,"
                 ":slug)")
    db.execute(query, {
        "username": user.username,
        "firstname": user.firstname,
        "lastname": user.lastname,
        "age": user.age,
        "slug": user.slug})
    db.commit()

    result = db.execute(select_query, {"username": user.username}).fetchone()
    return User(id=result.id, username=result.username, firstname=result.firstname, lastname=result.lastname,
                age=result.age, slug=result.slug)


@router.put('/update', response_model=User)
async def update_user(user_id: int, user: CreateUser, db: DbSession):
    select_query = text("SELECT * FROM users WHERE id = :id")
    result = db.execute(select_query, {"id": user_id}).fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    update_query = text(
        "UPDATE users SET username = :username, firstname = :firstname, lastname= :lastname, age= :age, slug = :slug WHERE id = :id"
    )
    db.execute(
        update_query,
        {
            "id": user_id,
            "username": user.username,
            "firstname": user.firstname,
            "lastname": user.lastname,
            "age": user.age,
            "slug": user.slug
        },
    )
    db.commit()
    # Возвращаем обновлённый продукт
    updated_result = db.execute(select_query, {"id": user_id}).fetchone()
    return User(
        id=updated_result.id,
        username=updated_result.username,
        firstname=updated_result.firstname,
        lastname=updated_result.lastname,
        age=updated_result.age,
        slug=updated_result.slug
    )


@router.get("/user_id/tasks")
async def tasks_by_user_id(user_id: int, db: DbSession):
    list_task = []
    select_query = text("SELECT * FROM tasks WHERE user_id = :user_id", )
    result = db.execute(select_query, {"user_id": user_id}).fetchall()
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    for task_user in result:
        list_task.append(Task(
            id=task_user.id,
            title=task_user.title,
            content=task_user.content,
            priority=task_user.priority,
            completed=task_user.completed,
            slug=task_user.slug,
            user_id=task_user.user_id
        ))
    return list_task


@router.delete('/delete/{category_id}')
async def delete_user(user_id: int, db: DbSession):
    select_query = text("SELECT * FROM users WHERE id = :id")
    result = db.execute(select_query, {"id": user_id}).fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    delete_query = text("DELETE FROM users WHERE id = :id")
    db.execute(delete_query, {"id": user_id})
    db.commit()

    select_query = text("SELECT * FROM tasks WHERE user_id = :user_id")
    result = db.execute(select_query, {"user_id": user_id}).fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    delete_query = text("DELETE FROM tasks WHERE user_id = :user_id")
    db.execute(delete_query, {"user_id": user_id})
    db.commit()

    return {"message": "User deleted"}
