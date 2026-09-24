from fastapi import HTTPException, status

from app.schemas.court import CourtIn
from app.models.court import Court


async def create_new_court(data: CourtIn):

    court = await Court.get_or_none(number=data.number)

    if court: 
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Identificação da quadra já existente.")

    court_created = await Court.create(
        number=data.number,
        description=data.description,
        price_per_hour=data.price_per_hour
    )    

    return court_created

async def get_all_courts():

    courts = await Court.all()

    return courts

async def get_court_by_id(court_id: int):

    court = Court.get_or_none(id=court_id)

    if court is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quadra não encontrada.")

    return court

async def update_court_by_id(court_id: int, data: CourtIn):

    court = await Court.get_or_none(id=court_id)

    if court is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quadra não encontrada.")

    if data.number is not None:
        court.number = data.number

    if data.description is not None:
        court.description = data.description

    if data.price_per_hour is not None:
        court.price_per_hour = data.price_per_hour     

    await court.save()

    return court

async def deactivate_court(court_id: int):

    court = await Court.get_or_none(id=court_id)

    if court is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quadra não encontrada.")

    court.is_active = False

    await court.save()

    return court


async def activate_court(court_id: int):

    court = await Court.get_or_none(id=court_id)

    if court is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Quadra não encontrada."
        )

    court.is_active = True

    await court.save()

    return court
