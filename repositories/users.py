from .base import BaseRepository
from db.users import users


class UserRepository(BaseRepository):

    async def get_all(limit: int=100, skip: int=0):
        return
    
    async def get_by_id(id:int):
        return
    
    async def creat():
        return
    
    async def update():
        return

    async def get_by_email(email: str):
        return