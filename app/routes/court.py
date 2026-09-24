from app.models.user import User, UserEnum
from app.core.dependecies import get_current_user
from fastapi import APIRouter, Depends, HTTPException, Query, status
from app.schemas.court import CourtIn, CourtOut
from app.models.user import User
from typing import Annotated

from app.services.court import create_new_court as create_new_court_service
from app.services.court import get_all_courts as get_all_courts_service
from app.services.court import get_court_by_id as get_court_by_id_service
from app.services.court import update_court_by_id as update_court_by_id_service
from app.services.court import deactivate_court as deactivate_court_service
from app.services.court import activate_court as activate_court_service

router = APIRouter(prefix="/courts", tags=["courts"])

@router.post("/", response_model=CourtOut, status_code=status.HTTP_201_CREATED)
async def create_new_court(data: CourtIn, current_user: Annotated[User, Depends(get_current_user)]):

    if current_user.role != UserEnum.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acesso não autorizado.")

    return await create_new_court_service(data)

@router.get("/", response_model=list[CourtOut], status_code=status.HTTP_200_OK)
async def get_all_courts(current_user: Annotated[User, Depends(get_current_user)]): 
    return await get_all_courts_service()

@router.get("/{court_id}", response_model=CourtOut, status_code=status.HTTP_200_OK)
async def get_court_by_id(current_user: Annotated[User, Depends(get_current_user)], court_id: int):
    return await get_court_by_id_service(court_id)

@router.patch("/{court_id}", response_model=CourtOut, status_code=status.HTTP_200_OK)
async def update_court_by_id(current_user: Annotated[User, Depends(get_current_user)], court_id: int, data: CourtIn):

    if current_user.role != UserEnum.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acesso não autorizado.")

    return await update_court_by_id_service(court_id)

@router.patch("/{court_id}/deactivate", response_model=CourtOut, status_code=status.HTTP_200_OK)
async def deactivate_court(current_user: Annotated[User, Depends(get_current_user)], court_id: int):

    if current_user.role != UserEnum.ADMIN:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acesso não autorizado.")

    return await deactivate_court_service(court_id)

@router.patch("/{court_id}/activate", response_model=CourtOut, status_code=status.HTTP_200_OK)
async def activate_court(current_user: Annotated[User, Depends(get_current_user)], court_id: int):

    if current_user.role != UserEnum.ADMIN:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acesso não autorizado.")    

    return await activate_court_service(court_id)
