import os
from fastapi import FastAPI, Form, Request
from fastapi.responses import  HTMLResponse

app = FastAPI()

@app.get("/")
def index(request: Request):  # функция. которая возвращает в браузер html-страницу
    index_file = os.path.join("static", "index.html")
    with open(index_file) as f:
        content = f.read()
        return HTMLResponse(content)
