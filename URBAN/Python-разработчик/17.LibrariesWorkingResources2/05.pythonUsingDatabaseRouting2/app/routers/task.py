from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import Annotated
from app.backend.db_depends import get_db
from sqlalchemy import insert, select, update
from app.schemas.task import Task, CreateTask
from slugify import slugify

router = APIRouter(prefix='/api/tasks', tags=['tasks'])

DbSession = Annotated[Session, Depends(get_db)]


@router.get('/', response_model=list[Task])
async def all_task(db: DbSession):
    query = text("SELECT * FROM tasks")
    result = db.execute(query).fetchall()
    return [Task(id=row.id, title=row.title, content=row.content, priority=row.priority,
                 completed=row.completed, slug=row.slug, user_id=row.user_id) for row in result]


@router.get('/user_id')
async def task_by_id(task_id: int, db: DbSession):
    select_query = text("SELECT * FROM tasks WHERE id = :id")
    result = db.execute(select_query, {"id": task_id}).fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return Task(
        id=result.id,
        title=result.title,
        content=result.content,
        priority=result.priority,
        completed=result.completed,
        slug=result.slug,
        user_id=result.user_id
    )


@router.post('/create', response_model=Task)
async def create_task(task: CreateTask, db: DbSession):
    query = text("INSERT INTO tasks (title, content, priority,completed, slug, user_id) VALUES"
                 "(:title, "
                 ":content, "
                 ":priority,"
                 ":completed, "
                 ":slug, "
                 ":user_id)")
    db.execute(query, {
        "title": task.title,
        "content": task.content,
        "priority": task.priority,
        "completed": task.completed,
        "slug": task.slug,
        "user_id": task.user_id})
    db.commit()

    select_query = text("SELECT * FROM tasks WHERE title = :title")
    result = db.execute(select_query, {"title": task.title}).fetchone()
    return Task(
        id=result.id,
        title=result.title,
        content=result.content,
        priority=result.priority,
        completed=result.completed,
        slug=result.slug,
        user_id=result.user_id,
    )


@router.put('/update', response_model=Task)
async def update_task(task_id: int, task: CreateTask, db: DbSession):
    select_query = text("SELECT * FROM tasks WHERE id = :id")
    result = db.execute(select_query, {"id": task_id}).fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    update_query = text(
        "UPDATE tasks SET title = :title, content = :content, priority= :priority, completed= :completed, slug = :slug, user_id= :user_id WHERE id = :id"
    )
    db.execute(
        update_query,
        {
            "id": task_id,
            "title": task.title,
            "content": task.content,
            "priority": task.priority,
            "completed": task.completed,
            "slug": task.slug,
            "user_id": task.user_id
        },
    )
    db.commit()
    # Возвращаем обновлённый продукт
    updated_result = db.execute(select_query, {"id": task_id}).fetchone()
    return Task(
        id=updated_result.id,
        title=updated_result.title,
        content=updated_result.content,
        priority=updated_result.priority,
        completed=updated_result.completed,
        slug=updated_result.slug,
        user_id=updated_result.user_id
    )


@router.delete('/delete/{category_id}')
async def delete_task(task_id: int, db: DbSession):
    select_query = text("SELECT * FROM tasks WHERE id = :id")
    result = db.execute(select_query, {"id": task_id}).fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    delete_query = text("DELETE FROM tasks WHERE id = :id")
    db.execute(delete_query, {"id": task_id})
    db.commit()
    return {"message": "Task deleted"}