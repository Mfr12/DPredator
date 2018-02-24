

from termcolor import colored
import os,socket

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

        print("{1}Phishing\n{2}Utilities\n{3}Information Grabbing\n{0}Exit")

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
            print("{1}Temporary Email\n{2}Fake Name Generator\n{3}CryptoCurrency\n{4}Domail to IP\n\n{0}Back to Main Menu")
            a = self.get()
            if a == 1:
                os.system("python EMail.py")
                DPredator()
            elif a == 2:
                import Fake
                DPredator()
            elif a == 3:
                import Crypto
                DPredator()
            elif a == 4:
                print("{Domain to IP}\n")
                domain = input("Enter your Domain: ")
                ip = socket.gethostbyaddr(domain)
                print("IP is: " + str(ip[2]))
                wait = input("\nPress [Enter] to go back...")
                DPredator()
            elif a == 0:
                DPredator()
        elif a == 3:
            os.system("clear")
            print("{Information Grabbing}\n")
            print("{1}Nmap\n")
            a = self.get()
            if a == 1:
                import Nmap
        elif a == "0":
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
