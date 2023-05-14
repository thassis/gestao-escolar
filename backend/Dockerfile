# pull official base image
FROM python:3.11.3-alpine

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# set work directory
WORKDIR /app/backend

# install dependencies
COPY requirements.txt /app/backend/
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . /app/backend/
