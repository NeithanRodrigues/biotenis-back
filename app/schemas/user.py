from datetime import date
from pydantic import BaseModel, EmailStr, model_validator
from app.models.user import UserEnum, AthleteClass
from typing import Optional


# User Register
class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone: str
    cpf: str
    birth_date: date
    role: UserEnum = UserEnum.VISITOR
    athlete_class: Optional[AthleteClass] = None

    @model_validator(mode="after")
    async def block_admin_register(user):
        if user.role == UserEnum.ADMIN:
            raise ValueError("Não é permitido se registrar como administrador.")
        return user
    
# Return of Register
class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    cpf: str
    birth_date: date
    athlete_class: Optional[AthleteClass] = None
    is_active: bool

    class Config:
        from_attributes = True

class UserUpdateSelf(BaseModel):
    phone: Optional[str] = None
    password: Optional[str] = None

class UserUpdateTeacher(BaseModel):
    athlete_class: Optional[AthleteClass] = None

class UserUpdateAdmin(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    role: Optional[UserEnum] = None
    athlete_class: Optional[AthleteClass] = None

