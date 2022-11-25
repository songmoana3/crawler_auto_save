FROM python:3.8.13-slim-buster

WORKDIR /app

COPY . /app

RUN useradd appuser -u 1000 -m -s /bin/bash
USER 1000

RUN pip install -r requirements.txt

WORKDIR /app/app

CMD ["python3","main.py","20220601","20220914"] 

