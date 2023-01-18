import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid =yOUR_sid
auth_token = YOUR_TOKEN
client = Client(account_sid, auth_token)

def send_massage(massage:str,to_num:str):
    message = client.messages.create(
                                  body=massage,
                                  from_=YOUR_NUMBER,
                                  to=to_num,
                          )
    print(message.status)
