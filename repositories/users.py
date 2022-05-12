import datetime
from .base import BaseRepository
from db.users import users
from typing import List, Optional
from models.user import User, UserIn
from core.security import hash_password


class UserRepository(BaseRepository):

    async def get_all(self, limit: int=100, skip: int=0) -> List[User]:
        query = users.select().limit(limit).offset(skip) 
        return await self.darabase.fetch_all(query=query)
    
    async def get_by_id(self, id:int) -> Optional[User]:
        query = users.select().where(users.c.id==id).first()
        user = await self.darabase.fetch_one(query) 
        if user is None:
            return None
        return User.parse_obj(user)
    
    async def creat(self, u:UserIn) -> User:
        user = User(
            name= u.name,
            email=u.email,
            name=u.name,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )

        values = {**user.dict()}
        values.pop("id",None)
        
        query = users.insert().values(**values)
        user.id = await self.darabase.execute(query)
        
        return user 
    
    async def update(self, u:UserIn) -> User:
        user = User(
            id=id,
            name= u.name,
            email=u.email,
            name=u.name,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )

        values = {**user.dict()}
        values.pop("id", None)
        values.pop("created_at", None)
        
        query = users.update().where(users.c.id==id).values(**values)
        await self.darabase.execute(query)
        
        return user 

    async def get_by_email(self, email: str) -> User:
        query = users.select().where(users.c.email==email).first()
        user = await self.darabase.fetch_one(query) 
        if user is None:
            return None
        return User.parse_obj(user)