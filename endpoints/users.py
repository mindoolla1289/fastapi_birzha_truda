from fastapi import APIRouter, Depends
from typing import List
from repositories.users import UserRepository
from models.user import User, UserIn
from .depends import get_users_repository

router = APIRouter()

@router.get("/")
async def read_users(limit: int =100, skip: int = 100):

    return{}