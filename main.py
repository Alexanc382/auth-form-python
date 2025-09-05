import os
from fastapi import FastAPI, Form
from fastapi.responses import  HTMLResponse
import sqlite3

app = FastAPI()


def init_db():
    conn = sqlite3.connect('users.db')
    curs = conn.cursor()
    curs.execute("""CREATE TABLE IF NOT EXISTS users (
                id integer PRIMARY KEY AUTOINCREMENT,
                username text NOT NULL,
                password text NOT NULL
            )
        """)
    conn.commit()
    conn.close()

init_db()


@app.get("/", response_class=HTMLResponse)
def index():  # функция. которая возвращает в браузер html-страницу
    index_file = os.path.join("static", "index.html")
    with open(index_file, "r", encoding="utf-8") as f:
        content = f.read()
        return HTMLResponse(content)


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    conn = sqlite3.connect('users.db')
    curs = conn.cursor()
    curs.execute("""INSERT INTO users (username, password) VALUES (?, ?)""", [username, password])
    conn.commit()
    conn.close()
    return {"message": "Login successful"}

