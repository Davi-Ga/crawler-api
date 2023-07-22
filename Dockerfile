FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r requirements.txt

# 
COPY ./app /app

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8686"]