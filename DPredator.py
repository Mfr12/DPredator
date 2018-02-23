#!/usr/bin/python

from termcolor import colored
import os

class DPredator:
    def __init__(self):
        os.system("clear")
        banner = """
    ██████╗  █████╗ ██████╗ ██╗  ██╗
    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝
    ██║  ██║███████║██████╔╝█████╔╝
    ██║  ██║██╔══██║██╔══██╗██╔═██╗
    ██████╔╝██║  ██║██║  ██║██║  ██╗
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
        """
        banner2 = """

        ██████╗ ██████╗ ███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗
        ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
        ██████╔╝██████╔╝█████╗  ██║  ██║███████║   ██║   ██║   ██║██████╔╝
        ██╔═══╝ ██╔══██╗██╔══╝  ██║  ██║██╔══██║   ██║   ██║   ██║██╔══██╗
        ██║     ██║  ██║███████╗██████╔╝██║  ██║   ██║   ╚██████╔╝██║  ██║
        ╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
        """
        print(banner + colored(banner2,'red'))
        print("Never So Late @M_F_R\n")

        print("{1}Phishing\n{2}Utilities")

        a = self.get()

        if a == 1:
            os.system("clear")
            print("{Phishing}\n")
            print("{1}SMS\n")
            a = self.get()
            if a == 1:
                import SMS
                DPredator()
        elif a == 2:
            os.system("clear")
            print("{Utilities}\n")
            print("{1}Temporary Email\n{2}Fake Name Generator\n")
            a = self.get()
            if a == 1:
                os.system("python EMail.py")
                DPredator()
            if a == 2:
                import Fake
                DPredator()

    def get(self):
        get = input("\nDPredator@ ")
        try:
            get = int(get)
        except:
            get = get
        os.system("clear")
        return get
if __name__ == '__main__':
    DPredator()
