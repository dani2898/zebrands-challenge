from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import app.config as conf
from app.presentation.routers import auth

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


app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Auth"]
)