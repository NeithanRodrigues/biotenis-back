from tortoise import fields
from tortoise.models import Model

from enum import Enum

class ReservationStatus(str, Enum):
    PENDING_PAYMENT = "pending_payment" 
    PAID = "paid"
    CANCELED = "canceled"
    COMPLETED = "completed"
    NO_SHOW = "no_show"

class CourtReservation(Model):
    id = fields.IntField(primary_key=True)
    user = fields.ForeignKeyField("models.User", related_name="reservations")
    court = fields.ForeignKeyField("models.Court", related_name="reservations")
    date = fields.DateField()
    start_time = fields.TimeField()
    end_time = fields.TimeField()
    status = fields.CharEnumField(ReservationStatus, default=ReservationStatus.PENDING_PAYMENT)
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)