FROM python:3.9-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apk add mariadb-dev build-base
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "uvicorn", "index:app", "--reload", "--host", "0.0.0.0", "--port", "8008"]
