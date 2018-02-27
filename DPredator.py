

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
        print(colored(banner,'white') + colored(banner2,'red'))
        print("Never So Late @M_F_R\n")

        print("{1}Phishing\n{2}Utilities\n{3}Information Grabbing\n{4}Social Engineering\n{5}Password Attacking\n\n{0}Exit")

        a = self.get()

        if a == 1:
            os.system("clear")
            print("{Phishing}\n")
            print("{1}SMS\n\n{0}Back to Main Menu")
            a = self.get()
            if a == 1:
                os.system("python3 Tools/SMS.py")
                DPredator()
            elif a == 0:
                DPredator()
        elif a == 2:
            os.system("clear")
            print("{Utilities}\n")
            print("{1}Temporary Email\n{2}Fake Name Generator\n{3}CryptoCurrency\n{4}Domail to IP\n\n{0}Back to Main Menu")
            a = self.get()
            if a == 1:
                os.system("python Tools/EMail.py")
                DPredator()
            elif a == 2:
                os.system("python3 Tools/Fake.py")
                DPredator()
            elif a == 3:
                os.system("python3 Tools/Crypto.py")
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
            print("{1}Nmap\n{2}WpScan\n{3}CMS Map (WordPress, Joomla, Drupal)\n{4}XSS Detection\n{5}Doork (Googling Tool)\n\n{0}Main Menu")
            a = self.get()
            if a == 1:
                os.system("python3 Tools/Nmap.py")
            elif a == 2:
                os.system("python3 Tools/WPSCAN.py")
            elif a == 3:
                os.system("python3 Tools/CMS.py")
            elif a == 4:
                os.system("python3 Tools/XSS.py")
            elif a == 5:
                os.system("python3 Tools/DORK.py")
            elif a == 0:
                DPredator()
        elif a == 4:
            os.system("clear")
            print("{Social Engineering}\n\n{1}QR Code\n\n{0}Main Menu")
            a = self.get()
            if a == 1:
                os.system("python3 Tools/QRCODE.py")
            elif a == 0:
                DPredator()
        elif a == 5:
            os.system("clear")
            print("{Passwords Attacking}\n\n{1}Common User Passwords Profiler\n\n{0}Main Menu")
            a = self.get()
            if a == 1:
                os.system("python3 Tools/CUPP.py")
            '''elif a == 2:
                os.system("python3 Tools/BRUTEX.py")'''
        elif a == 0:
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
