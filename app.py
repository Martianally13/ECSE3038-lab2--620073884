from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

fake_database = []

origins = [
  "https://ecse-week3-demo.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/todos")
async def get_all_todos():
    return fake_database

@app.post("/todos")
async def create_todos(request: Request):
    todo = await request.json()
    fake_database.append(todo)
    return todo

@app.patch("/todos/{id}")
async def update_by_id(id: int, request: Request):
    todo_update = request.json()
    for todo in fake_database:
        if todo["id"] == id:
            todo.update(todo_update)
            return todo
             
    raise HTTPException(status_code=404, detail="Object not found")
            

@app.delete("/todos/{id}")
async def delete_todo_by_id(id: int, request: Request):
    todo_update = request.json()
    for todo in fake_database:
        if todo["id"] == id:
            fake_database.remove(todo)
            return {"Message":"Object has been deleted"}
         
    raise HTTPException(status_code=404, detail="Object not found")
            
            

