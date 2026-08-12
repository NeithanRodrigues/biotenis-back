from fastapi import APIRouter, status

from app.schemas.user import UserOut, UserIn
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth import register as register_service
from app.services.auth import login as login_service

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register(user: UserIn):
    return await register_service(user)

@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def login(user: LoginRequest):
    return await login_service(user)