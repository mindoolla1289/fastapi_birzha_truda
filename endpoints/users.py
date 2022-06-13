from fastapi import APIRouter, Depends
from typing import List
from repositories.users import UserRepository
from models.user import User, UserIn
from .depends import get_users_repository

router = APIRouter()

@router.get("/", response_model= List[User])
async def read_users(
    users: UserRepository = Depends(get_users_repository),
    limit: int =100,
    skip: int = 0):
    
    return await users.get_all(limit=limit, skip=0)

@router.post("/", response_model=User)
async def create_user(user: UserIn, users: UserRepository = Depends(get_users_repository)): 
    return await users.create(u=user)

@router.put("/", response_model=User)
async def update_user(id: int, user: UserIn, users: UserRepository = Depends(get_users_repository)): 
    return await users.update(id=id, u=user)