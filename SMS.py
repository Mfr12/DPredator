#!/usr/bin/python

import os
from kavenegar import *
from twilio.rest import Client

def get():
    get = input("\nDPredator@ ")
    try:
        get = int(get)
    except:
        get = get
    os.system("clear")
    return get

print("Choose your Method:\n{1} Kavenegar\n{2} Twillo")
method = get()
os.system("clear")
print("Enter your Message: ")
mess = get()
print("Enter your Victim Phone Number (With +98): ")
phone = get()
if method == 1:
    try:
        api = KavenegarAPI('Put Your API Key Here')
        params = {
        'sender': '',
        'receptor': str(phone).replace("+98","0"),
        'message' : mess
        }
        response = api.sms_send(params)
        print("Your Message has been sent!")
    except:
        print("An Error Occurred")
    wait = input("Press [Enter] to go back...")
elif method == 2:
    try:
        account_sid = "Put Your Sid Account Token Here"
        auth_token = "Put Your auth_token Here"

        client = Client(account_sid, auth_token)

        client.api.account.messages.create(
            to = phone,
            from_ = "+17606385101",
            body = mess)
        print("Your Message has been sent!")
    except:
        print("An Error Occurred")
    wait = input("Press [Enter] to go back...")
