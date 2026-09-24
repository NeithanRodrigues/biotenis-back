from datetime import datetime, timedelta
from decimal import Decimal

from fastapi import HTTPException, status
from tortoise.transactions import in_transaction

from app.models.court import Court
from app.models.court_reservation import CourtReservation
from app.models.court_reservation import ReservationStatus
from app.models.user import User
from app.schemas.court_reservation import AdminCourtReservationOut, CourtReservationIn, MyCourtReservationOut

async def create_reservation(current_user: User, data: CourtReservationIn):

    court = await Court.get_or_none(id=data.court_id, is_active=True)

    if court is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quadra não encontrada ou inativa.",
        )

    new_start_time = datetime.combine(data.date, data.start_time)
    new_end_time = datetime.combine(data.date, data.end_time)
    hours = (new_end_time - new_start_time).total_seconds() / 3600
    final_price = court.price_per_hour * Decimal(str(hours))

    # Verifica se existe uma reserva pra essa quadra, na data X.
    # Verifica se o horário de início da Reserva existente, é menor que o horário da nova
    # Exemplo (Existente_Início = 10:00 < Final_Nova= 12:00 → Passa)
    # AND Verifica se o horário final da reserva existente, é maior que o horário da nova
    # Exemplo (Existente_Final = 11:00 > Nova_Início = 10:30 → Não passa)
    async with in_transaction():
        check_exists = await CourtReservation.select_for_update().filter(
            court_id=data.court_id,
            date=data.date,
            start_time__lt=data.end_time,
            end_time__gt=data.start_time,
        ).exists()

        if check_exists:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Horário já reservado para essa quadra.")

        reservation = await CourtReservation.create(
            user_id=current_user.id,
            court_id=data.court_id,
            date=data.date,
            start_time=data.start_time,
            end_time=data.end_time,
            price=final_price 
        )

        return MyCourtReservationOut(
            court_id=court.id,
            court_number=court.number,
            court_description=court.description,
            date=reservation.date,
            start_time=reservation.start_time,
            end_time=reservation.end_time,
            status=reservation.status,
            price=reservation.price,
            created_at=reservation.created_at,
        )

async def get_my_reservations(current_user: User):

    reservations = await (
        CourtReservation
        .filter(user_id=current_user.id)
        .select_related("court")
        .all())

    return [
        MyCourtReservationOut(
            court_id=item.court.id,
            court_number=item.court.number,
            court_description=item.court.description,
            date=item.date,
            start_time=item.start_time,
            end_time=item.end_time,
            status=item.status,
            price=item.price,
            created_at=item.created_at,
        )
        for item in reservations
    ]

async def admin_get_all_reservations(offset: int = 0, limit: int = 30):

    reservations = await (
        CourtReservation
        .all()
        .select_related("court","user")
        .offset(offset)
        .limit(limit)
    )

    return [
        AdminCourtReservationOut(
            id=item.id,
            user_id=item.user.id,
            user_name=item.user.name,
            user_phone=item.user.phone,
            court_id=item.court.id,
            court_number=item.court.number,
            court_description=item.court.description,
            date=item.date,
            start_time=item.start_time,
            end_time=item.end_time,
            status=item.status,
            price=item.price,
            created_at=item.created_at,
        )
        for item in reservations
    ]

async def cancel_reservation(current_user: User, reservation_id: int):

    reservation = await ( 
    CourtReservation
    .filter(id=reservation_id, user_id=current_user.id)
    .select_related("court")
    .first()
    
    )
    if reservation is None: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reserva não encontrada."
        )

    if reservation.status == ReservationStatus.CANCELED:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Esta reserva já foi cancelada.",
        )

    reservation_datetime = datetime.combine(reservation.date, reservation.start_time)
    if reservation_datetime - datetime.now() < timedelta(hours=2):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cancelamento só é permitido com pelo menos 2 horas de antecedência.",
        )

    reservation.status = ReservationStatus.CANCELED
    await reservation.save()

    return MyCourtReservationOut(
        court_id=reservation.court.id,
        court_number=reservation.court.number,
        court_description=reservation.court.description,
        date=reservation.date,
        start_time=reservation.start_time,
        end_time=reservation.end_time,
        status=reservation.status,
        price=reservation.price,
        created_at=reservation.created_at,
    )
