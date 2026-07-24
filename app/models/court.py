from tortoise.models import Model
from tortoise import fields


class Court(Model):
    id = fields.IntField(primary_key=True)
    number = fields.IntField(unique=True)
    description = fields.CharField(max_length=500, null=True)
    price_per_hour = fields.DecimalField(max_digits=10, decimal_places=2)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    