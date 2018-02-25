#!/usr/bin/python

import os

repeat = "y"
class NMAP:
    def __init__(self):
        check = os.path.isfile("/usr/bin/nmap") or os.path.isfile("/usr/local/bin/nmap")
        if not check:
            os.system("cd Tools && mkdir Nmap && cd Nmap && git clone https://github.com/nmap/nmap.git && cd nmap && ./configure && make && make install")
        os.system("clear")
        host = input("Enter your Host (or either...): ")
        os.system("clear")
        print("{Nmap}\nHost: " + host + "\n{1}Simple Scan\n{2}Port Scan\n{3}OS Detection\n{0}Main Menu")
        a = self.get()
        if a == 1:
            os.system("nmap -sV " + host)
        elif a == 2:
            os.system("nmap -Pn " + host)
        elif a == 3:
            os.system("nmap -A " + host)
        a = input("Do you want to try again?[Y/n] ")
        if a == "y" or a == "Y":
            NMAP()
        else:
            global repeat
            repeat = "n"
    def get(self):
        get = input("\nDPredator@ ")
        try:
            get = int(get)
        except:
            get = get
        os.system("clear")
        return get
        return get
while True:
    if repeat == "y":
        NMAP()
