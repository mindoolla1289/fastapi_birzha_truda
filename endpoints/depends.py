from repositories.users import UserRepository
from db.base import dbase

def get_users_repository()-> UserRepository:
    return UserRepository(dbase)
