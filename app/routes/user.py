from typing import Annotated
from fastapi import APIRouter, Depends, Query, status, HTTPException
from app.core.dependecies import get_current_user
from app.schemas.user import UserOut
from app.models.user import User, UserEnum

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserOut)
async def get_user(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user

@router.get("/students", response_model=list[UserOut])
async def get_all_students(user: Annotated[User, Depends(get_current_user)], 
    offset: int=0, 
    limit: Annotated[int, Query(le=30)] = 30):

    if user.role not in [UserEnum.ADMIN, UserEnum.TEACHER]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acesso não autorizado.")    

    users = await User.filter(role=UserEnum.STUDENT).offset(offset).limit(limit).all()
    return users

