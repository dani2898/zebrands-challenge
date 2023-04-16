from datetime import timedelta

from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

import app.config as conf


class Settings(BaseModel):
    authjwt_algorithm: str = "RS512"
    public_key: str = conf.RSA_KEYS["PUBLIC_KEY"]
    private_key: str = conf.RSA_KEYS["PRIVATE_KEY"]
    authjwt_access_token_expires: int = timedelta(minutes=conf.ACCESS_TOKEN_EXPIRE_MINUTES)


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(request, credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    @staticmethod
    def verify_jwt(request: Request, token) -> bool:
        is_token_valid: bool = False
        auth_jwt = AuthJWT(request, token)
        try:
            payload = auth_jwt.get_raw_jwt()
        except RuntimeError as e:
            raise HTTPException(
                status_code=500, detail=str(e))
        except Exception:
            payload = None
        if payload:
            is_token_valid = True
        return is_token_valid

@AuthJWT.load_config
def get_config():
    return Settings()
