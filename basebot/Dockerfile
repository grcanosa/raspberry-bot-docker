FROM python:3.6-stretch

LABEL author_name Gonzalo Rodriguez
LABEL author_email grcanosa@gmail.com

RUN apt-get update -y
RUN apt-get install -y python3 python-pip-whl python3-pip

COPY requirements.txt .

RUN pip3 install -r requirements.txt

WORKDIR /code