import os
from dotenv import load_dotenv
import smtplib
from twilio.rest import Client
from config import *


class NotificationManager:
    def __init__(self):
        
        load_dotenv()
        self.account_sid : str = os.getenv('TWILIO_SID')
        self.auth_token : str = os.getenv('TWILIO_AUTH_TOKEN') 
        self.from_ : str = os.getenv('TWILIO_VIRTUAL_NUMBER') 
        self.to : str = os.getenv('TWILIO_VERIFIED_NUMBER') 
        self.mail_sender : str = os.getenv('MAIL_SENDER') 
        self.mail_sender_pw : str = os.getenv('MAIL_SENDER_PW') 
         
        self.client = Client(self.account_sid, self.auth_token)
      
    def send_sms(self, message):
        message = self.client.messages.create(
            body=f"({CURRENT_DATE})New Low Price Flight!\n{message}\n\nMore Infomation:\n{GOOGLE_SHEEET_URL}",
            from_ = self.from_, 
            to = self.to
            )
        print(message.sid)
    
    def send_mails(self, date, send_to, message):
        mail_subject = f"Low Price Flight! ({CURRENT_DATE})"
        mail_body = f'More Infomation:\n{GOOGLE_SHEEET_URL}\n----------------------\n' + message
        
        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.ehlo("smtp.office365.com")
            server.starttls()
            server.login(user=self.mail_sender, password=self.mail_sender_pw)
            
            server.sendmail(
                from_addr=self.mail_sender,
                to_addrs=send_to,
                msg=f'Subject: {date}_{mail_subject}\n\n{mail_body}\n'.encode("utf-8")
                )
        print('mail sent successfully!')


if __name__ == "__main__":
    test = NotificationManager()
    # with open(MAIL_RECODE_FILE) as data:
    #     message = data.read()
    #     test.send_mails(CURRENT_DATE, 'xxxx@gmail.com', message)
    #     test.send_sms('Hello world')
    
