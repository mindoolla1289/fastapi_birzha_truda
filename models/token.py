from pydantic import BaseModel, EmailStr


class Token (BaseModel):
    access_string: str 
    token_type: str

class Login(BaseModel):
    emain: EmailStr
    password: str
