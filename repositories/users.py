from .base import BaseRepository
from db.users import users
from typing import List
from models.user import User, UserIn


class UserRepository(BaseRepository):

    async def get_all(self, limit: int=100, skip: int=0) -> List[User]:
        return
    
    async def get_by_id(self, id:int) -> User:
        return
    
    async def creat(self, u:UserIn) -> User:
        return
    
    async def update(self, u:UserIn) -> User:
        return

    async def get_by_email(self, email: str) -> User:
        return