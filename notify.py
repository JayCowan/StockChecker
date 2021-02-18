import os
import const
from twilio.rest import Client
from dotenv import load_dotenv

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
load_dotenv()
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


def notify(dict):
    try:
        message = client.messages \
                    .create(
                        body=dict['title'] + " with stock of " + dict['stock'] + " at " + dict['link'],
                        from_=const.TWILIO_NUMBER,
                        to=const.PHONE_NUMBER
                    )
        print(message.sid)
    except TypeError:
        print("TypeError has occured while trying to notify.")
def notify_error(message):
    try:
        client.messages.create(body=message, from_=const.TWILIO_NUMBER, to=const.PHONE_NUMBER)
    except:
        print("An exception has occured while trying to notify the user of a program exception")
