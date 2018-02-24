#!/usr/bin/python

import os
from DPredator import DPredator

check = os.path.isdir("wpscan")
if not check:
    os.system("git clone https://github.com/wpscanteam/wpscan.git")
os.system("clear")
host = input("Enter your Host (or either...): ")
host = "--no-banner --random-agent --url " + host
os.system("clear")

print("{WP Scan}\n{1}User Enumeration\n{2}Plugin Enumeration\n{3}Enumerate All\n{0}Main Menu")
a = int(input())
if a == 1:
    os.system("cd wpscan && ruby wpscan.rb " + host + " --enumerate u")
elif a == 2:
    os.system("ruby wpscan/wpscan.rb " + host + " --enumerate p")
elif a == 3:
    os.system("ruby wpscan/wpscan.rb " + host + " --enumerate")
elif a == 0:
    pass
DPredator()
