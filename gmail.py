from email import message
import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
from helper import *
from time import sleep
load_dotenv()




class Gmail:

    def __init__(self, email_address, password):
        self.email_address = email_address
        self.password = password

        try:
            self.smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            self.smtp.login(self.email_address, self.password)
            print("Connected to GMAIL successfully")
            self.connection = True
        except:
            print("\nFaild to connect to GMAIL")
            self.connection = False

    def send_email(self, reciever, sender, subject, txt, file, CL='None', Trans='None'):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = reciever
        msg.add_alternative(f'{txt}', subtype = 'html')
        
        try:
            with open(file, 'rb') as f:
                file_data = f.read()
                msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename='CV.pdf')
            if CL == 1:
                cl = 'Cover Letter.pdf'
                with open(cl, 'rb') as ff:
                    file_data = ff.read()
                    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename='Cover Letter.pdf')

            if Trans == 1:
                transcript = 'Transcript.pdf'
                with open(transcript, 'rb') as fff:
                    file_data = fff.read()
                    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename='Transcript.pdf')

            self.smtp.send_message(msg)
            print(f"✅ Email sent to {reciever}")
            return f"✅ Email sent to {reciever}", True
        except:
            print(f"❌ Failed to send email to {reciever}")
            return f"❌ Failed to send email to {reciever}", False

    def close_gmail(self):
        self.smtp.close()

