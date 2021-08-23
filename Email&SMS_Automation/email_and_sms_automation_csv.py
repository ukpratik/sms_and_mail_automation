from dotenv import load_dotenv
from email_message import mail_message
from send_email import send_email
from twilio_sms_api import send_sms
import content_template

load_dotenv()

DEBUGGING = True
excel_filename = 'Final_Sheet-Table 1.csv'
sheet_name = 'Final Sheet'
awb_number = "A"
num_of_entries = 0
num_of_fields = 0

all_entries = []

with open(excel_filename) as file:
    entries = file.read().split('\n')

for entry in entries:
    data = entry.split(',')
    ORDER_ID = data[0]
    AWB_NUMBER = data[1]
    INVOICE_LINK = data[2]
    EMAIL_ID = data[3]
    MOBILE_NUMBER = data[4]
    PRODUCT_NAME = data[5]
    CUSTOMER_NAME = data[6]
    TRACKING_ID = data[7]
    TRACKING_LINK = data[8]

    if ORDER_ID == 'Order ID':
        continue

    if MOBILE_NUMBER[0] != '+':
        MOBILE_NUMBER = '+' + MOBILE_NUMBER

    print(ORDER_ID)

    email_filled_template = content_template.email_body_template(CUSTOMER_NAME,TRACKING_ID,TRACKING_LINK,INVOICE_LINK)
    mail_body = mail_message(subject="Order Shipped",text=email_filled_template)
    send_email(EMAIL_ID,mail_body)

    sms_filled_template = content_template.sms_body_template(CUSTOMER_NAME,TRACKING_ID,TRACKING_LINK,INVOICE_LINK)
    send_sms(to=MOBILE_NUMBER,body=sms_filled_template)


