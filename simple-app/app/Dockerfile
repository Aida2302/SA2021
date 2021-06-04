FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY . /code

WORKDIR /code

CMD ["flask", "run"]