from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todo_list = []


class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool = False


# Add a new todo item to the list.
@app.post("/todo")
def create_todo_item(todo_item: TodoItem):
    todo_list.append(todo_item)
    return {"message": "Todo item created successfully.", "data": todo_item}


# Get all todo items
@app.get("/todo")
def get_all_todo_items():
    return {"message": "Todo items retrieved successfully.", "data": todo_list}


# Get a specific todo item by its ID
@app.get("/todo/{todo_id}")
def get_todo_item(todo_id: int):
    for todo_item in todo_list:
        if todo_item.id == todo_id:
            return {"message": "Todo item retrieved successfully.", "data": todo_item}

    return {"message": f"Todo item with ID {todo_id} not found."}


# Update a specific todo item
@app.put("/todo/{todo_id}")
def update_todo_item(todo_id: int, updated_todo: TodoItem):
    for index, existing_todo in enumerate(todo_list):
        if existing_todo.id == todo_id:
            todo_list[index] = updated_todo

            return {"message": "Todo item updated successfully.", "data": updated_todo}

    return {"message": f"Todo item with ID {todo_id} not found."}


# Delete a specific todo item
@app.delete("/todo/{todo_id}")
def delete_todo_item(todo_id: int):
    for index, todo_item in enumerate(todo_list):
        if todo_item.id == todo_id:
            deleted_item = todo_list.pop(index)

            return {"message": "Todo item deleted successfully.", "data": deleted_item}

    return {"message": f"Todo item with ID {todo_id} not found."}
