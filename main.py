from fastapi import FastAPI

from .models import User


# API
app = FastAPI()


users = []



@app.get("/")
async def home():
    return "Hello World"

@app.get("/users")
async def get_users():
    return users


@app.post("/users")
async def post_users(user : User):
    users.append(user)
    return {"message": "added"}