import os
from typing import Annotated
from fastapi import FastAPI
from app.core.database import init_db
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from app.routes import auth

app = FastAPI()
init_db(app)

app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Servidor rodando..."}
