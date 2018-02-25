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
print("{SMS Phishing}\n")
print("Choose your Method:\n{1} Kavenegar\n{2} Twillo\n\n{0}Back to Main Menu")
method = get()
if method == 0:
    os.system("clear")
else:
    os.system("clear")
    print("Enter your Message: ")
    mess = get()
    print("Enter your Victim Phone Number (With +98): ")
    phone = get()
    if method == 1:
        try:
            api = KavenegarAPI('334164386C6A79304F6D6B597645744D5765634D4A686161676E696864493965')
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
            account_sid = "AC550e96a4047b7b3ac04217e3d40745d2"
            auth_token = "9f482b34cacad639a4c185e81e0cd625"

            client = Client(account_sid, auth_token)

            client.api.account.messages.create(
                to = phone,
                from_ = "+17606385101",
                body = mess)
            print("Your Message has been sent!")
        except:
            print("An Error Occurred")
        wait = input("Press [Enter] to go back...")
        os.system("python3 DPredator.py")
