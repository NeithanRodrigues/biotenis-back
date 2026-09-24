from fastapi import HTTPException, status

from app.core.security import hash_password
from app.models.user import User, UserEnum
from app.schemas.user import UserUpdateAdmin, UserUpdateSelf

async def self_update(data: UserUpdateSelf, current_user: User) -> User:
    if data.phone is not None: 
        current_user.phone = data.phone

    if data.password is not None: 
        current_user.hash_password = hash_password(data.password)

    await current_user.save()
    return current_user    

async def get_all_students(offset: int = 0, limit: int = 30):

    students = await User.filter(role=UserEnum.STUDENT).offset(offset).limit(limit).all()

    return students

async def get_students_by_id(student_id: int):

    student = await User.get_or_none(id=student_id)

    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado.")

    return student

async def get_all_users(offset: int = 0, limit: int = 30):

    users = await User.all().offset(offset).limit(limit)

    if users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não foi possível coletar os usuários.")

    return users 

async def get_user_by_id(user_id: int):

    user = await User.get_or_none(id=user_id)

    if user is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado.")

    return user

async def update_user(data: UserUpdateAdmin, user_id: int):

    user = await User.get_or_none(id=user_id)

    if user is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado.")

    if data.name is not None: 
        user.name = data.name

    if data.email is not None: 
        user.email = data.email

    if data.phone is not None: 
        user.phone = data.phone

    if data.athlete_class is not None:
        user.athlete_class = data.athlete_class

    if data.role is not None:
        user.role = data.role

    await user.save()

    return user

async def deactivate_user(user_id: int):

    user = await User.get_or_none(id=user_id)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado.")

    user.is_active = False

    await user.save()

    return user


async def activate_user(user_id: int):

    user = await User.get_or_none(id=user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado."
        )

    user.is_active = True

    await user.save()

    return user
