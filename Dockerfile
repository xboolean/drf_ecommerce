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

COPY ./entrypoint.sh /usr/src/app/
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# CMD ["uwsgi", "--http", ":8080", "--ini", "./uwsgi/uwsgi.ini"]
COPY . /usr/src/app/
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]