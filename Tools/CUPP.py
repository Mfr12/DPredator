#!/usr/bin/python
import os
from termcolor import colored

path = open("path.txt","r")
path = path[0]

if os.path.isdir(path + "/Tools/cupp") == True:
    print("{Cupp}\n\nMake dictionary file for your victim:")
    os.system("cd " + path + "/Tools/cupp && python cupp.py -i")
else:
    os.system("cd " + path + "/Tools && git clone https://github.com/Mebus/cupp.git")
    os.system("cd " + path + "/Tools/cupp && python cupp.py -i")

print(colored("\n","white"))
os.system("cd " + path + "/Tools/cupp && echo You can access your dictionary in: $PWD")
wait = input("Press [Enter] to go back...")
os.system("python3 DPredator.py")
