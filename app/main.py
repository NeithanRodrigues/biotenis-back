import os
from fastapi import FastAPI
from app.core.database import init_db
from app.routes import auth, court, user

app = FastAPI()
init_db(app)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(court.router)


@app.get("/")
async def root():
    return {"message": "Servidor rodando..."}
