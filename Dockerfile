FROM python:3.10.1-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update \
  && apt-get -y install netcat gcc \ 
  && apt-get -y install nano \
  && apt-get clean

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --verbose -r requirements.txt

COPY . /usr/src/app/