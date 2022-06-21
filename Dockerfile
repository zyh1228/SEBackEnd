FROM python:3.8-alpine3.16

ENV SERVER_ENV production

ADD . /app
WORKDIR /app

HEALTHCHECK --interval=5s --retries=3 CMD python3 /app/deploy/health_check.py

RUN apk add --update --no-cache build-base nginx openssl curl unzip supervisor jpeg-dev zlib-dev postgresql-dev freetype-dev && \
    pip install --no-cache-dir -r /app/deploy/requirements.txt && \
    apk del build-base --purge

ENTRYPOINT /app/deploy/entrypoint.sh
