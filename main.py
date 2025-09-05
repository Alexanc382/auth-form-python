from fastapi import FastAPI, Form, Request
from fastapi.responses import  HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

