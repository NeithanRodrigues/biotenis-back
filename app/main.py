import os
from typing import Annotated
from fastapi import FastAPI
from app.core.database import init_db
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
init_db(app)


@app.get("/")
async def root():
    return {"message": "Servidor rodando..."}
