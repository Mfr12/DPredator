#!/usr/bin/python

import os

if os.path.isdir("Tools/CMSmap") == True:
    pass
else:
    os.system("git clone https://github.com/Dionach/CMSmap.git")
host = input("{CMS Map}\n\nEnter Your Host: ")
os.system("cd Tools/CMSmap && python cmsmap.py -t " + host)
wait = input("Press [Enter] to go back...")
os.system("python3 DPredator.py")
