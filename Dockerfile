FROM python:3.12
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 POETRY_VIRTUALENVS_CREATE=false

RUN pip install --no-cache-dir poetry==1.5.0

ENV PYTHONPATH=/app

WORKDIR /app
COPY pyproject.toml /app

