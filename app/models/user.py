from tortoise.models import Model
from tortoise import fields

from enum import Enum
from enum import IntEnum

class UserEnum(str, Enum):
    TEACHER = "teacher"
    STUDENT = "student"
    VISITOR = "visitor"
    ADMIN = "admin"

class AthleteClass(IntEnum):
    CLASS_1 = 1
    CLASS_2 = 2
    CLASS_3 = 3 
    CLASS_4 = 4
    CLASS_5 = 5
    CLASS_6 = 6

class User(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)
    hash_password = fields.CharField(max_length=255)
    phone = fields.CharField(max_length=20)
    cpf = fields.CharField(max_length=14, unique=True)
    birth_date = fields.DateField()
    role = fields.CharEnumField(UserEnum, default=UserEnum.VISITOR)
    athlete_class = fields.IntEnumField(AthleteClass, null=True)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)