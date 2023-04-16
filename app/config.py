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

# JWT TOKEN
# ------------------------------------------------------------------------------
ACCESS_TOKEN_EXPIRE_MINUTES = 15  # One Week

RSA_KEYS = {
    "PUBLIC_KEY": os.getenv("PUBLIC_KEY"),
    "PRIVATE_KEY": os.getenv("PRIVATE_KEY"),
}

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


class Settings(BaseModel):
    authjwt_algorithm: str = "RS512"
    authjwt_public_key: str = RSA_KEYS["PUBLIC_KEY"]
    authjwt_private_key: str = RSA_KEYS["PRIVATE_KEY"]
    authjwt_access_token_expires: int = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

@AuthJWT.load_config
def get_config():
    return Settings()