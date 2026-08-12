from app.models.user import User
from app.schemas.auth import LoginRequest
from app.schemas.user import UserIn
from app.core.security import create_access_token, hash_password, verify_password

from tortoise.expressions import Q

from fastapi import HTTPException, status

async def register(user: UserIn):

    exists = await User.get_or_none(Q(email=user.email) | Q(cpf=user.cpf))
    if exists: 
        if exists.email == user.email:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email já registrado.")
        else: 
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CPF já cadastrado.")

    hashed = hash_password(user.password)

    user_created = await User.create(
        name=user.name,
        email=user.email,
        hash_password=hashed,
        phone=user.phone,
        cpf=user.cpf,
        birth_date=user.birth_date,
        role=user.role,
        athlete_class=user.athlete_class,
    )

    return user_created

async def login(data: LoginRequest):

    user = await User.get_or_none(email=data.email)

    if not user or not verify_password(data.password, user.hash_password): 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas.")

    token  = create_access_token({"sub": str(user.id)})

    return {"access_token": token, "token_type": "bearer"}

     

    
    