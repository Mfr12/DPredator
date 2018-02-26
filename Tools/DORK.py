import os

def install(a):
    try:
        import a
    except:
        os.system("sudo pip install " + a)
if os.path.isdir("Tools/doork") == True:
    pass
else:
    os.system("cd Tools && git clone https://github.com/AeonDave/doork doork")
install("beautifulsoup4")
install("Django")
install("requests")
os.system("clear")
host = input("{Doork}\n\nEnter your Host Name (With http://wwww.): ")
os.system("cd Tools/doork && python 2 doork.py -t " + host)
wait = input("Press [Enter] to go back...")
os.system("python3 DPredator.py")
