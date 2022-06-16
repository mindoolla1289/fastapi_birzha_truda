from fastapi import Depends, HTTPException, status
from models.user import User
from core.security import JWTBearer, decode_access_token
from repositories.users import UserRepository
from db.base import dbase

def get_users_repository()-> UserRepository:
    return UserRepository(dbase)

async def get_current_user(
    users: UserRepository= Depends(get_users_repository),
    token: str = Depends(JWTBearer()),
)-> User:
    cred_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credentials are not valid")
    payload = decode_access_token(token)
    if payload is None:
        raise cred_exception
    email: str = payload.get("sub")
    if email is None:
        raise cred_exception
    user = await users.get_by_email(email=email)
    if user is None:
        return cred_exception
    return user