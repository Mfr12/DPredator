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

        print("{1}Phishing\n{2}Utilities\n\n{exit}Exit")

        a = self.get()

        if a == 1:
            os.system("clear")
            print("{Phishing}\n")
            print("{1}SMS\n\n{0}Back to Main Menu")
            a = self.get()
            if a == 1:
                import SMS
                DPredator()
            elif a == 0:
                DPredator()
        elif a == 2:
            os.system("clear")
            print("{Utilities}\n")
            print("{1}Temporary Email\n{2}Fake Name Generator\n\n{0}Back to Main Menu")
            a = self.get()
            if a == 1:
                os.system("python EMail.py")
                DPredator()
            elif a == 2:
                import Fake
                DPredator()
            elif a == 0:
                DPredator()
        elif a == "exit":
            os.system("exit")

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
