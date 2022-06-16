from starlette.config import Config

config = Config(".env")

DATABASE_URL = config("EE_DATABASE_URL", cast=str, default=True)
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("EE_SECRET_KEY", cast=str,default="f25b59a18bf4cd5b172a3beafc1b123155874a16d28abe30a1bb0c15d16401dd")  
