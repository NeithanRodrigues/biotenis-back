from tortoise.contrib.fastapi import register_tortoise
from app.core.config import DATABASE_URL


def init_db(app):

    register_tortoise(
        app,
        db_url=DATABASE_URL,
        modules={"models": ["app.models"]},
        generate_schemas=True,
        add_exception_handlers=True
    )