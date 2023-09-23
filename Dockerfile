FROM python:3.10.10-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update && apk add chromium chromium-chromedriver

RUN apk add --no-cache --virtual build-dependencies libpq-dev build-base

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt -vvv 

COPY . /app

RUN chmod +w .

EXPOSE 8686

# ENTRYPOINT ["sh", "entrypoint.sh"]
