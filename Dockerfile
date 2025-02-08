FROM python:3.12-slim

LABEL maintainer="AISSMS"
LABEL version="1.0"
LABEL description="This is a Dockerfile for a Python Django application"

ENV PYTHONUNBUFFERED 1 

WORKDIR /app

COPY ./requirements.txt /requirements.txt
COPY ./models/models.joblib /models/models.joblib 
COPY ./webapp /app/webapp

EXPOSE 8000 

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    rm -rf /root/.cache && \
    adduser --disabled-password --no-create-home appuser

ENV PATH="/py/bin:$PATH"
USER appuser
