FROM python:3.10.5-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN apt-get update -qq && apt-get install -y postgresql-client

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --verbose -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

RUN adduser --system --group nruser
USER nruser

CMD gunicorn root.wsgi:application --bind 0.0.0.0:$PORT