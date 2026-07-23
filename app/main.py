import os
from fastapi import FastAPI
from app.core.database import init_db

app = FastAPI()
init_db(app)

@app.get("/")
async def root():
    return {"message": "Servidor rodando..."}