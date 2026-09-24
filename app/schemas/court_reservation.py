from decimal import Decimal

from pydantic import BaseModel, model_validator
from datetime import date, datetime, time

from app.models.court_reservation import ReservationStatus

class CourtReservationIn(BaseModel):
    court_id: int
    date: date
    start_time: time
    end_time: time

    @model_validator(mode="after")
    def validate_time_range(self):
        if self.start_time >= self.end_time:
            raise ValueError("O horário de término (end_time) deve ser maior que o horário de início (start_time).")

        return self

class MyCourtReservationOut(BaseModel):
    court_id: int
    court_number: int
    court_description: str
    date: date
    start_time: time
    end_time: time
    status: ReservationStatus
    price: Decimal
    created_at: datetime

    class Config:
        from_attributes = True

class AdminCourtReservationOut(BaseModel):
    user_id: int
    user_name: str
    user_phone: str

    court_id: int
    court_number: int
    court_description: str

    id: int
    date: date
    start_time: time
    end_time: time
    status: ReservationStatus
    price: Decimal
    created_at: datetime

    class Config:
            from_attributes = True