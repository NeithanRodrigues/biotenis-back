from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "hash_password" VARCHAR(255) NOT NULL,
    "phone" VARCHAR(20) NOT NULL,
    "cpf" VARCHAR(14) NOT NULL UNIQUE,
    "birth_date" DATE NOT NULL,
    "role" VARCHAR(7) NOT NULL,
    "athlete_class" SMALLINT,
    "is_active" BOOL NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL,
    "updated_at" TIMESTAMPTZ NOT NULL
);
COMMENT ON COLUMN "user"."role" IS 'TEACHER: teacher\nSTUDENT: student\nVISITOR: visitor\nADMIN: admin';
COMMENT ON COLUMN "user"."athlete_class" IS 'CLASS_1: 1\nCLASS_2: 2\nCLASS_3: 3\nCLASS_4: 4\nCLASS_5: 5\nCLASS_6: 6';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmG1v4jgQgP9KlE9daW8FlMKKb4HmVE68nEq6d9rtyTKJIVYTOxs7fdFu//vaTkxISF"
    "Koju5u1U+Y8Yw9eWbssf3NDKmHAvbhiqHYHBjfTAJDJBoF+XvDhFGUS6WAw2WgFBOtsWQ8"
    "hi4XshUMGBIiDzE3xhHHlAgpSYJACqkrFDFZ56KE4K8JApyuEfeVH1/+E2JMPHSPmP4b3Y"
    "AVRoFXcBN7cm4lB/whUrIx4X8qRTnbErg0SEKSK0cP3Kdko40Jl9I1IiiGHMnheZxI96V3"
    "2VfqL0o9zVVSF7dsPLSCScC3PncJcpkJwGzugIXtAGAeAMilRMIVrjL19Wvpwh+ddrff/X"
    "ja634UKsrNjaT/mE6dg0kNFZ6ZYz6qfshhqqEY51DV7w7WkQ/jaq5av0RWuFwmqzk2odWC"
    "nG2eTy8BN4T3IEBkzX1J9OysAeUn63J0YV2eCK13ckoqFkC6KmZZVyftk7xzviiEODgE8M"
    "bg/yH8c5P3+Hx9yHwQQcbuaFyxP9Rz3jF8y+j9iEeC0kFbxsbgNRJu7QO4Vc+3VcbrRqtD"
    "4Gbqr26zaHf3ANvu1oKVXUWwSxxzH4hCWJG850JazbdoVcIsxRyH6IPu/81yuQHxueXYJY"
    "AxDWrWvU2SUOEbi+EhcdEORm37cluAeYsZ5jQ2D2NnOrY1urAvRe4j6IoT6jVZOFfn9swZ"
    "GIwnHiL8mnwaL8bOXOhkc1wT63w6ng0M6IWYmM9I96ZDnM72fm2y98u5DrkfII6AG4gCV3"
    "lqfjpkO2M8fZiuiF22gxw5483RxFosQFvsG9ckbXfE5qzbpwPjVLe7A6Or22cD40y3ewOj"
    "t2fk0iP5aaff25zG5Z+mGC6m1mSiT+NbVxoGxDUK31asqyEVSwaSmtvNtl0pLktheKxFpe"
    "vBy+5Fw/l8IkcOGfsaKMHYKS2Fq+nQFvVArRChhHma5zvA3RhJJADy6iIgd/OaQluwbCoE"
    "svEbFgNTfKA3J8FDFueGgDjjqb1wrOnfhajIkiF7Okr6UJKe9Erb12YQ45+xc2HIv8bn+c"
    "xWeCnj61jNmOs5n03pE0w4BYTeAehtHVG0VFMrRD2JvGdGvWj5FvVfJeqa0VbYlffy8Wh1"
    "s/XSIQVL6N7cwdgDOz20Q+t0d7vCTliWQALXKmYSrnQze0qzUIxd36x4ZMt63jc9s8Fc5+"
    "2h7cUWwpEf2m5RzKRLlQfoarRbJq/x6nyMxwm5qA4gnKm/Qrrt1j4vE0Kr/gbd2n2boIQj"
    "UlFE/1rMZzXHptykXD2xy43vRoDZPveIX412A1wJo1AiNdOTqfVvGfdoMh+Wa58cYCjQ/9"
    "Ri9vgDFS9VAA=="
)
