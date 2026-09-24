from typing import Annotated
from fastapi import APIRouter, Depends, Query, status, HTTPException
from app.core.dependecies import get_current_user
from app.schemas.user import UserOut, UserUpdateAdmin, UserUpdateSelf, UsertOutForTeacher
from app.models.user import User, UserEnum

from app.services.user import self_update as self_update_service
from app.services.user import get_all_students as get_all_students_service
from app.services.user import get_students_by_id as get_students_by_id_service 
from app.services.user import get_all_users as get_all_users_service
from app.services.user import get_user_by_id as get_user_by_id_service
from app.services.user import update_user as update_user_service
from app.services.user import deactivate_user as deactivate_user_service
from app.services.user import activate_user as activate_user_service

router = APIRouter(prefix="/users", tags=["users"])


# ---------- MYSELF ROUTES ----------

@router.get("/me", response_model=UserOut, status_code=status.HTTP_200_OK)
async def get_user(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@router.patch("/me", response_model=UserOut, status_code=status.HTTP_200_OK)
async def update_me(current_user: Annotated[User, Depends(get_current_user)], data: UserUpdateSelf):
    return await self_update_service(current_user, data)


# ---------- TEACHERS ROUTES ----------

@router.get("/students", response_model=list[UsertOutForTeacher], status_code=status.HTTP_200_OK)
async def get_all_students(current_user: Annotated[User, Depends(get_current_user)], offset: int = 0, limit: Annotated[int, Query(le=30)] = 30): 
    if current_user.role != UserEnum.TEACHER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acesso não autorizado.")

    return await get_all_students_service(offset, limit)


@router.get("/students/{student_id}", response_model=UsertOutForTeacher, status_code=status.HTTP_200_OK)
async def get_students_by_id(current_user: Annotated[User, Depends(get_current_user)], student_id: int):
    if current_user.role != UserEnum.TEACHER:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acesso não autorizado.")
    return await get_students_by_id_service(student_id)


# ---------- ADMINS ROUTES ----------

@router.get("/", response_model=UserOut, status_code=status.HTTP_200_OK)
async def get_all_users(current_user: Annotated[User, Depends(get_current_user)], offset: int = 0, limit: Annotated[int, Query(le=30)] = 30):
    if current_user.role != UserEnum.ADMIN:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acessou não autorizado.")
    return await get_all_users_service(offset, limit)


@router.get("/users/{user_id}", response_model=UserOut, status_code=status.HTTP_200_OK)
async def get_user_by_id(current_user: Annotated[User, Depends(get_current_user)], user_id: int):
     if current_user.role != UserEnum.ADMIN: 
          raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acesso não autorizado.")

     return await get_user_by_id_service(user_id)


@router.patch("/users/{user_id}", response_model=UserOut, status_code=status.HTTP_200_OK)
async def update_user(current_user: Annotated[User, Depends(get_current_user)], user_id: int, data: UserUpdateAdmin):

     if current_user.role != UserEnum.ADMIN:
          raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acesso não autorizado.")

     return await update_user_service(data, user_id)

@router.patch("/users/{user_id}/deactivate", response_model=UserOut, status_code=status.HTTP_200_OK)
async def deactivate_user(current_user: Annotated[User, Depends(get_current_user)], user_id: int):

    if current_user.role != UserEnum.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acesso não autorizado.")     

    return await deactivate_user_service(user_id)


@router.patch("/users/{user_id}/activate",response_model=UserOut,status_code=status.HTTP_200_OK,)
async def activate_user(current_user: Annotated[User, Depends(get_current_user)], user_id: int):

    if current_user.role != UserEnum.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acesso não autorizado.")

    return await activate_user_service(user_id)
