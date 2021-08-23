from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
MOBILE_NUMBER = os.environ.get('MOBILE_NUMBER')
DEBUGGING = True

def send_sms(to,body,from_=MOBILE_NUMBER):
    print(ACCOUNT_SID)
    print(AUTH_TOKEN)
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    print("sending sms ...")
    MOBILE_NUMBER=from_
    if MOBILE_NUMBER[0] != '+':
        MOBILE_NUMBER = '+' + MOBILE_NUMBER
    message = client.messages.create(body=body,from_=from_,to=to)
    print(message.sid)
    print('sms sent.')
