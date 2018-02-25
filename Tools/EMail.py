#!/usr/bin/python

import time, os
from tempMail import tempMail

email = tempMail.mailer()
email_address = email.getEmail()
print("{Temporary Email}\n")
print("if you want to exit type [Control + C]")
print("Your E-Mail address is: " + email_address)
print("Wait Until Emails sent...")

while True:
    result = email.mailBox()
    if result:
        print("Sender: " + result["Sender"])
        print("Subject: " + result["Subject"])
        ask = raw_input("Do you want to see email? [Y/n] ")
        if ask == "y" or ask == "Y":
            html = file(result["Sender"].replace(" ","") + ".html","w")
            body = result["body"]
            html.write(body)
            html.close()
            os.system('open -a "Google Chrome" ' + result["Sender"].replace(" ","") + ".html")
        ask = raw_input("Do you want to Keep it? [Y/n] ")
        if ask == "n" or ask == "N":
            os.system("rm " + result["Sender"].replace(" ","") + ".html")
    time.sleep(5)
