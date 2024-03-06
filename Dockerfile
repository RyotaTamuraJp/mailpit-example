FROM python:3.11.1-slim-bullseye

ENV PYTHONPATH=/app
ENV LANG ja_JP.UTF-8

WORKDIR /app

COPY ./app ./

RUN apt-get update \
  && apt-get upgrade -y \
  && pip install -U pip \
  && pip install poetry \
  && poetry run pip install -U pip setuptools \
  && poetry install \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

CMD [ "/app/start.sh" ]
