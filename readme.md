# FastAPI Todo API

Ce projet est un exemple simple d'API Todo construite avec FastAPI. Il permet de gérer une liste de tâches (Todo) avec des opérations CRUD (Créer, Lire, Mettre à jour, Supprimer).

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- [Python 3.7+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

## Installation

Suivez les étapes ci-dessous pour configurer et lancer le projet sur votre machine locale.

Tout d'abord, installez FastAPI et Uvicorn :

1. Créer un environnement virtuel (optionnel)
```
python -m venv env
source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`
```

2. Installer FastAPI et Uvicorn
```
pip install fastapi uvicorn
```

## Structure du projet
Créez une structure de projet qui sépare les éléments principaux :

```
my_fastapi_todo/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── routes.py
├── run.py
```

## Run
Après avoir écrire les models, les routes, vous pouvez lancer votre projet en utilisant la commande:

```
uvicorn app.main:app --reload
```

### Exemple
1. Modèles (models.py)
Créez les modèles Pydantic pour représenter les données de votre todo dans models.py :


```
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    title: str
    description: str = None
    completed: bool = False
```

2. Routes (routes.py)
Définissez les routes de votre API dans routes.py :

```
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
```

3. Initialisation de l'application (main.py)
Dans main.py, importez les routes et créez l'application FastAPI :

```
from fastapi import FastAPI
from .routes import router as todo_router

app = FastAPI()

app.include_router(todo_router)
```
