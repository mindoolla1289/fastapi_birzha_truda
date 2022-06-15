from  passlib.context import CryptContext
import datetime
from jose import jwt 
from .config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password:str, hash: str) -> str:
    return pwd_context.verify_password(password, hash)


def create_access_token(data:dict) -> str:
    to_encode= data.copy()
    to_encode.update({"exp":datetime.datetime.utcnow()+ datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

def decode_access_token(token:str):
    try:
        encode_jwt= jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
    except jwt.JWSError:
        return None
    return encode_jwt
