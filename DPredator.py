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

        print("{1}Phishing\n")

        if self.get() == 1:
            os.system("clear")
            print("{1}SMS\n{2}E-Mail\n")
            if self.get() == 1:
                import SMS
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
