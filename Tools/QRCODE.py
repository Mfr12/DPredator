#!/usr/bin/python
import os

try:
    import qrcode
except:
    os.system("pip3 install qrcode")

a = input("{QR Code}\n\nEnter your text: ")
qr = qrcode.make(a)
qr.show()
wait = input("Press [Enter] to go back...")
os.system("python3 DPredator.py")
