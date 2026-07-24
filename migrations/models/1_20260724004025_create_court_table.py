from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "court" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "number" INT NOT NULL UNIQUE,
    "description" VARCHAR(500),
    "price_per_hour" DECIMAL(10,2) NOT NULL,
    "is_active" BOOL NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL,
    "updated_at" TIMESTAMPTZ NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "court";"""


MODELS_STATE = (
    "eJztmW1v2joUgP9KlE+d1FsB5WXiW6CZyhUvVyXdpt1eWSYxxGriZInTrtr632c7MYG8Dd"
    "BghcunmuNzbOc5ts857nfV9SzkhFf3IQrUrvJdJdBFrLEmv1RU6PuplAsonDlCMZIas5AG"
    "0KRMNodOiJjIQqEZYJ9ijzApiRyHCz2TKWKySEURwV8jBKi3QNQW6/j3PybGxELfUCh/+o"
    "9gjpFjrS0TW3xuIQf0xReyAaEfhCKfbQZMz4lckir7L9T2yFIbE8qlC0RQACniw9Mg4svn"
    "q0u+Un5RvNJUJV7iio2F5jBy6MrnzkAqUwEYTwww1Q0A1C0AmR7hcNlSQ/H1C76Evxr1Zq"
    "f5/rrdfM9UxDKXks5rPHUKJjYUeMaG+ir6IYWxhmCcQhV/c1j7NgyKuUr9DFm25CxZybEK"
    "rRSkbNP9dAi4LvwGHEQW1OZEW60KlB+1u/6tdnfBtN7xKT12AOJTMU66GnEf553yRS7Ezj"
    "aAlwa/h/Cf3bz752vD0AY+DMNnLyi4H8o55wzPO3oz4j6jtNWVsTQ4RcK1TQDXyvnWsnhN"
    "f74N3ET95C6LenMDsPVmKVjetQ52hgNqAxYICzbvDZMW8123ymDmYopddCX7j2wvVyC+0Q"
    "w9AzDwnJJzr5PIFfgGbHhITJTDKG0PdwWoTzjE1AvU7diphq71b/U7tvcRNFmG+kCmxv2N"
    "Pja6SkgjCxH6QD4OpgNjwnSSOR6IdjMajLsKtFxM1B22e1USJ3d7p3Szd7J7HVLbQRQB02"
    "EBrjBr/rXLcmP8Opku8F1yg+x5x6v9oTadgjq7Nx5I3G6wy1m2r7vKtWw3u0pTtltdpSXb"
    "7a7S3tBzcUp+3ei0l9k4/1Hlw+lIGw5lNr5S0oSAlVH4qeBc9Tx2ZCApqW5W7TJ+mTHDfR"
    "0qGQ8Oexf1JpMhH9kNw6+OEAyMzFG4H/V0Fg/ECWFKmMb7PAfcDBBHAiAtDgL8Ni8JtGuW"
    "VYGAN44wGKjsA60JcV4SP1c4xBiM9Kmhjf5Z8woPGbynIaQvGelFO3N9LQdRPg2MW4X/VL"
    "5MxrrA64V0EYgZUz3ji8rXBCPqAeI9A2itpChSKqmteT3yrR29vm559vpb8bpktOJ2sXr+"
    "eDR/XHnp4IIZNB+fYWCBXI/X8Mp0811uw81KIIEL4TMOly8zeUrre1FA1YI3trjjsuqRzV"
    "yqnF/ZDnYK9v3KFrmz+Ol0Q7CpwU5Z1ynSTWmuLqOwHilmmjHbqRQ5TDq7Y83cqm3yGsG0"
    "SgsJ0Zd57gmwiYCPAmCzi6kgfiITu9ApefrJGWdDaGx9lYxyhAG0qobW+wOW91/Ua5eNTG"
    "YqndHM8T6XBOeS4K3s7SNNDs8lwf/R62+8JNAQi4W2WlATJD2VRQFMdc5VwXHlreVVwRMK"
    "wi1z2BWTU/xv2j7+X8kP1RaEE/UTpFvfqDyoV5QH9Xx5wGakiBQE0b+nk3FJ2pSaZKMnNq"
    "nyQ3FwuFOR+3YrAQ5jLURKphcj7XMWd3846WVjHx+gx9D/0WD2+hOSHy6S"
)
