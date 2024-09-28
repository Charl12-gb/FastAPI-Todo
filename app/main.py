from fastapi import FastAPI
from .routes import router as todo_router

app = FastAPI()

app.include_router(todo_router)
