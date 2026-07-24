from tortoise.contrib.fastapi import register_tortoise
from app.core.config import DATABASE_URL

TORTOISE_ORM = {
    "connections": {
        "default": DATABASE_URL,
    },
    "apps": {
        "models": {
            "models": [
                "app.models.user",
                "app.models.court",
                "app.models.court_reservation",
                "aerich.models",
                ],
            "default_connection": "default",
            "migrations": "migrations",
        },
    },
}

def init_db(app):

    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False,
        add_exception_handlers=True
    )