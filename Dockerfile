# ubuntu: 20.04を使用
FROM ubuntu:20.04

COPY requirement.txt /app/requirement.txt
COPY .env /app/.env
COPY message.json /app/message.json
COPY send_email_2.py /app/send_email_2.py

# パッケージのインストール
RUN apt update && \
    apt install -y python3 python3-pip iputils-ping net-tools curl tcpdump &&\
    pip3 install -r /app/requirement.txt

WORKDIR /app
