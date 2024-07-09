# ubuntu: 20.04を使用
FROM ubuntu:20.04

COPY requirement.txt /app/requirement.txt
COPY send_email.py /app/send_email.py

# パッケージのインストール
RUN apt update && \
    apt install -y python3 python3-pip iputils-ping net-tools curl tcpdump &&\
    pip3 install -r /app/requirement.txt

WORKDIR /app
