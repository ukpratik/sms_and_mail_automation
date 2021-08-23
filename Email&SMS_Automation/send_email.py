import smtplib
import os
import ssl
from dotenv import load_dotenv

load_dotenv()
CONTEXT = ssl.create_default_context()
EMAIL_ID = os.environ.get('EMAIL_ID')
PASSWORD = os.environ.get('PASSWORD')
SMTP_SERVER = os.environ.get('SMTP_SERVER')

SMTP_PORT = os.environ.get('SMTP_PORT')
SMTP_PORT = int(SMTP_PORT)

def send_email(to,body):
    smtp = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
    # print('4')
    smtp.ehlo()  # send the extended hello to our server
    smtp.starttls(context=CONTEXT)  # tell server we want to communicate with TLS encryption
    # print('5')
    smtp.login(EMAIL_ID, PASSWORD)  # login to our email server
    # print('6')
    # send our email message 'msg' to our boss
    smtp.sendmail(EMAIL_ID,to,str(body))
    # print('7')             
    smtp.quit()  # finally, don't forget to close the connection