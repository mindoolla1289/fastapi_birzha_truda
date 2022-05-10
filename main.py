from fastapi import FastAPI
from db.base import dbase
import uvicorn 


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.on_event("startup")
async def startup():
    await dbase.connect()

@app.on_event("shutdown")
async def shutdown():
    await dbase.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)