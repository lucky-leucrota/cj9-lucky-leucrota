from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import chat

app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(chat.router)
