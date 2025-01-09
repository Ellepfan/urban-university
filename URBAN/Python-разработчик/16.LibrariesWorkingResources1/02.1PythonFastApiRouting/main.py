from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return f"Главная страница"

@app.get("/user/admin")
async def admin_user():
    return f"Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user_id(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user/")
async def user(username:str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст {age}"
