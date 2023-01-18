import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC6cfe0cdea4775d8cadfd4e2023228325'
auth_token = '9950f4656985fc96fdac23b7ea65e520'
client = Client(account_sid, auth_token)

def send_massage(massage:str,to_num:str):
    message = client.messages.create(
                                  body=massage,
                                  from_='+18059024520',
                                  to=to_num,
                          )
    print(message.status)
