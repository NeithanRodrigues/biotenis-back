from fastapi import APIRouter, status, Query, Depends, HTTPException
from typing import Annotated

from app.core.dependecies import get_current_user
from app.models.court_reservation import ReservationStatus
from app.models.user import User, UserEnum
from app.schemas.court_reservation import AdminCourtReservationOut, CourtReservationIn, MyCourtReservationOut

from app.services.court_reservation import create_reservation as create_reservation_service
from app.services.court_reservation import get_my_reservations as get_my_reservations_service
from app.services.court_reservation import admin_get_all_reservations as admin_get_all_reservations_service
from app.services.court_reservation import cancel_reservation as cancel_reservation_service

router = APIRouter(prefix="/reservations", tags=["reservations"])

@router.post("/", response_model=MyCourtReservationOut, status_code=status.HTTP_201_CREATED)
async def create_reservation(current_user: Annotated[User, Depends(get_current_user)], data: CourtReservationIn):

    return await create_reservation_service(current_user, data)

@router.get("/me", response_model=list[MyCourtReservationOut], status_code=status.HTTP_200_OK)
async def get_my_reservations(current_user: Annotated[User, Depends(get_current_user)]):

    return await get_my_reservations_service(current_user)

@router.patch("/{reservation_id}/cancel", response_model=MyCourtReservationOut, status_code=status.HTTP_200_OK)
async def cancel_reservation(current_user: Annotated[User, Depends(get_current_user)], reservation_id: int):

    return await cancel_reservation_service(current_user, reservation_id)

# ADMIN ROUTES

@router.get("/", response_model=list[AdminCourtReservationOut], status_code=status.HTTP_200_OK)
async def get_all_reservations(current_user: Annotated[User, Depends(get_current_user)], offset: int = 0, limit: Annotated[int, Query(le=30)] = 30):

    if current_user.role not in [UserEnum.ADMIN, UserEnum.TEACHER]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acesso não autorizado.")

    return await admin_get_all_reservations_service(offset, limit) 
