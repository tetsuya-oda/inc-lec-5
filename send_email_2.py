from smtplib import SMTP

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

from dotenv import load_dotenv

import os
import ssl
import schedule
import time
import json


load_dotenv()

gmail_addr = os.getenv('GMAIL_ADDRESS')
app_passwd = os.getenv('APP_PASSWD')
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = os.getenv('SMTP_PORT')

from_addr = gmail_addr
to_addr = gmail_addr

def load_message(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['messages']


def send_email(subject, body):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    context=ssl.create_default_context()

    with SMTP(smtp_server, smtp_port) as smtp:
        try:
            print("メール送信中...")
            smtp.starttls(context=context)
            smtp.login(gmail_addr, app_passwd)
            smtp.send_message(msg)
            print("メール送信完了")
        except Exception as e:
            print(e)
            print("メール送信失敗")


def schedule_email(messages):
    current_hour = datetime.now().hour + 9
    for message in messages:
        if message['hour'] == current_hour:
            send_email(message['subject'], message['body'])


if __name__ == '__main__':
    messages = load_message('message.json')
    schedule.every().hour.at(':00').do(schedule_email, messages)

    while True:
        schedule.run_pending()
        time.sleep(1)
