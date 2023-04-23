# pull official base image
FROM python:3.11.3-alpine

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# set work directory
WORKDIR /app/backend

# Build psycopg2-binary from source
RUN apk add --virtual .build-deps --no-cache postgresql-dev gcc python3-dev musl-dev && \
        apk --purge del .build-deps

# install dependencies
COPY requirements.txt /app/backend/
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . /app/backend/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
