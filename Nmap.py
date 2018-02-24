#!/usr/bin/python

import os

check = os.path.isfile("/usr/bin/nmap") or os.path.isfile("/usr/local/bin/nmap")
if not check:
    os.system("cd Tools && mkdir Nmap && cd Nmap && git clone https://github.com/nmap/nmap.git && cd nmap && ./configure && make && make install")
os.system("clear")
host = input("{Nmap}\nEnter your Host (or either...): ")
