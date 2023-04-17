FROM python:3.9-alpine3.13

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY poetry.lock pyproject.toml /code/

RUN apk add --update --upgrade --no-cache --virtual .build-deps \
    build-base \
    musl-dev \
    postgresql-dev \
    gcc \
    libpq \
    zlib-dev \
    libffi-dev \
    glib \
    ca-certificates \
    nano \
    curl \
    openssl-dev \
    cargo

RUN pip install poetry

RUN poetry install

COPY . .
