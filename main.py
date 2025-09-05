import os
from fastapi import FastAPI, Form
from fastapi.responses import  HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():  # функция. которая возвращает в браузер html-страницу
    index_file = os.path.join("static", "index.html")
    with open(index_file, "r", encoding="utf-8") as f:
        content = f.read()
        return HTMLResponse(content)

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    entered_name = username
    entered_password = password
    user_data = {
        "username": entered_name,
        "password": entered_password
    }
    return user_data