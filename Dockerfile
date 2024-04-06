FROM python:3.12.2-alpine3.19@sha256:c7eb5c92b7933fe52f224a91a1ced27b91840ac9c69c58bef40d602156bcdb41

WORKDIR ./app

COPY ./randomgen ./randomgen
COPY app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt
EXPOSE 8080

CMD python -m flask run -h '0.0.0.0' -p 8080