from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "courtreservation" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "date" DATE NOT NULL,
    "start_time" TIMETZ NOT NULL,
    "end_time" TIMETZ NOT NULL,
    "status" VARCHAR(15) NOT NULL,
    "price" DECIMAL(10,2) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL,
    "updated_at" TIMESTAMPTZ NOT NULL,
    "court_id" INT NOT NULL REFERENCES "court" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "courtreservation"."status" IS 'PENDING_PAYMENT: pending_payment\nPAID: paid\nCANCELED: canceled\nCOMPLETED: completed\nNO_SHOW: no_show';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "courtreservation";"""


MODELS_STATE = (
    "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"
    "g="
)
