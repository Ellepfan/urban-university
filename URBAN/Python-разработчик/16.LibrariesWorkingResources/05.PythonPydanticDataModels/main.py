from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel
from typing import List
import warnings

warnings.simplefilter("ignore", DeprecationWarning)

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
async def users_dict() -> List[User]:
    return users


@app.post("/user/{username}/{age}", response_model=User)
async def add_users(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UserUrban")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=1)]):
    new_id = int(max((t.id for t in users), default=0)) + 1
    user = User(id=new_id, username=username, age=age)
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
async def user_update(user_id: Annotated[int, Path(ge=0, le=100, description="Enter User ID", example=1)],
                      username: Annotated[
                          str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]) -> str:
    for i in users:
        if i.id == user_id:
            users[user_id - 1] = User(id=user_id, username=username, age=age)
            return f"he user {user_id} is updated"
    else:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def user_del(user_id: Annotated[int, Path(ge=0, le=100, description="Enter User ID", example=1)]):
    for i in users:
        if i.id == user_id:
            users.pop(user_id - 1)
            return f"User {user_id} has been deleted"
    else:
        raise HTTPException(status_code=404, detail=f"User was not found")
