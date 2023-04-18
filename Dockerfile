FROM python:3.10-alpine

COPY ./ /ChatGPT-Customer-Service
WORKDIR /ChatGPT-Customer-Service

RUN apk add --no-cache \
    build-base \
    gcc \
    g++
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]