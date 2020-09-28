FROM python:3.8-slim-buster AS uwsgi

ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN echo "deb http://mirrors.aliyun.com/debian buster main contrib non-free" > /etc/apt/sources.list && \
    echo "deb-src http://mirrors.aliyun.com/debian buster main contrib non-free" >> /etc/apt/sources.list  && \
    echo "deb http://mirrors.aliyun.com/debian buster-updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb-src http://mirrors.aliyun.com/debian buster-updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/debian-security buster/updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb-src http://mirrors.aliyun.com/debian-security buster/updates main contrib non-free" >> /etc/apt/sources.list

RUN apt-get -y update && apt-get install -y gcc

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD uwsgi --ini uwsgi.ini
