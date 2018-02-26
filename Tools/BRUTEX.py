#!/usr/bin/python
import os


if os.path.isdir("/usr/share/brutex") == False:
    os.system("/usr/share/brutex")
    os.system("cd Tools && git clone https://github.com/1N3/BruteX.git")

os.system("sudo cd Tools/BruteX && echo $PWD && ls")
a = input("Enter Your IP: ")
os.system("brutex " + a)
