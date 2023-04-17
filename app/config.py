import os

from urllib.parse import quote_plus

from dotenv import load_dotenv

from pydantic import BaseModel

from datetime import timedelta

from fastapi_jwt_auth import AuthJWT

load_dotenv()


# MIDDLEWARE
# ------------------------------------------------------------------------------
ALLOW_CROS_ORIGINS = [
    "*",
]

# POSTGRES DB
# ------------------------------------------------------------------------------
HOST_POSTGRES = os.getenv("HOST_POSTGRES")
USER_POSTGRES = os.getenv("USER_POSTGRES")
PASSWORD_POSTGRES = os.getenv("PASSWORD_POSTGRES")
DB_POSTGRES = os.getenv("DB_POSTGRES", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
SQL_PROTOCOL = "postgresql+psycopg2"

SQLALCHEMY_DATABASE_URL = '{}://{}:{}@{}:{}/{}'.format(
    SQL_PROTOCOL,
    USER_POSTGRES,
    quote_plus(str(PASSWORD_POSTGRES)),
    HOST_POSTGRES,
    DB_PORT,
    DB_POSTGRES
)