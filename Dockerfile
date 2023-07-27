FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update && apk add chromium chromium-chromedriver

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r requirements.txt

ENV CHROME_DRIVER_PATH=/usr/bin/chromedriver
ENV CHROME_BIN=/usr/bin/chromium-browser

COPY ./app /app

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8686"]