import os

from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "database": os.environ.get("POSTGRES_DB"),
                "host": os.environ.get("POSTGRES_HOST"),
                "password": os.environ.get("POSTGRES_PASSWORD"),
                "port": os.environ.get("POSTGRES_PORT"),
                "user": os.environ.get("POSTGRES_USER"),
            },
        }
    },
    "apps": {
        "models": {
            "models": ["currency.models"],
            "default_connection": "default",
        }
    },
}
