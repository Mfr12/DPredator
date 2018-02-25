#!/usr/bin/python
import os
from DPredator import DPredator

try:
    import qrcode
except:
    os.system("pip3 install qrcode")

a = input("{QR Code}\n\nEnter your text: ")
qr = qrcode.make(a)
qr.show()
wait = input("Press [Enter] to go back...")
DPredator()
