import os
import smtplib
from twilio.rest import Client
from config import *


class NotificationManager:
    def __init__(self):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.client = Client(account_sid, auth_token)
      
    def send_sms(self, message):
        message = self.client.messages.create(
            body=f"({CURRENT_DATE})New Low Price Flight!\n{message}\n\nMore Infomation:\n{GOOGLE_SHEEET_URL}",
            from_ = os.environ['TWILIO_VIRTUAL_NUMBER'],
            to = os.environ['TWILIO_VERIFIED_NUMBER']
            )
        print(message.sid)
    
    def send_mails(self, date, send_to, message):
        mail_sender = os.environ['MAIL_SENDER']
        mail_sender_pw = os.environ['MAIL_PASSWORD']
        mail_subject = f"Low Price Flight! ({CURRENT_DATE})"
        mail_body = f'More Infomation:\n{GOOGLE_SHEEET_URL}\n----------------------\n' + message
        
        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.ehlo("smtp.office365.com")
            server.starttls()
            server.login(user=mail_sender, password=mail_sender_pw)
            
            server.sendmail(
                from_addr=mail_sender,
                to_addrs=send_to,
                msg=f'Subject: {date}_{mail_subject}\n\n{mail_body}\n'.encode("utf-8")
                )
        print('mail sent successfully!')


if __name__ == "__main__":
    test = NotificationManager()
    # with open(MAIL_RECODE_FILE) as data:
    #     message = data.read()
    #     test.send_mails(CURRENT_DATE, SEND_TO, message)
    #     test.send_sms('Hello world')
    