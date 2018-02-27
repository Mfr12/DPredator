#!/usr/bin/python
import os
from termcolor import colored


if os.path.isdir("Tools/cupp") == True:
    print("{Cupp}\n\nMake dictionary file for your victim:")
    os.system("cd Tools/cupp && python cupp.py -i")
else:
    os.system("cd Tools && git clone https://github.com/Mebus/cupp.git")
    os.system("cd Tools/cupp && python cupp.py -i")

print(colored("\n","white"))
os.system("cd Tools/cupp && echo You can access your dictionary in: $PWD")
wait = input("Press [Enter] to go back...")
os.system("python3 DPredator.py")
