from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException

import app.config as conf
from app.presentation.routers import auth, user, product

app = FastAPI(
    title="Zebrands Backend",
    description="Catalog system",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=conf.ALLOW_CROS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(
    request: Request,
    exc: AuthJWTException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Auth"]
)

app.include_router(
    user.router,
    prefix="/user",
    tags=["User"]
)

app.include_router(
    product.router,
    prefix="/product",
    tags=["Product"]
)