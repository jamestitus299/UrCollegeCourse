from fastapi import FastAPI, Path, APIRouter
from typing import List, Optional
from .models import User

router = APIRouter()

users = []

@router.get("/users", response_model=List[User])
async def get_users():
    return users


@router.post("/users")
async def post_users(user : User):
    users.append(user)
    return {"message": "added"}


@router.get("/users/{id}")
def get_user_by_id(id : int = Path(..., description="The id of the User you want to query.", gt=-1)):
    return users[id]