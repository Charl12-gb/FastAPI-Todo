from fastapi import APIRouter, HTTPException
from typing import List

from .models import Todo

router = APIRouter()

# Liste des todos
todos: List[Todo] = []

@router.get("/todos/", response_model=List[Todo])
def get_todos():
    return todos

@router.post("/todos/", response_model=Todo)
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@router.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    todo = next((todo for todo in todos if todo.id == todo_id), None)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo):
    todo_index = next((index for index, todo in enumerate(todos) if todo.id == todo_id), None)
    if todo_index is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    todos[todo_index] = updated_todo
    return updated_todo

@router.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int):
    todo = next((todo for todo in todos if todo.id == todo_id), None)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    todos.remove(todo)
    return todo
