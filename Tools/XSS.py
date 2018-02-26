import os

if os.path.isdir("Tools/XSStrike") == True:
    pass
else:
    os.system("cd Tools && git clone https://github.com/UltimateHackers/XSStrike")
os.system("cd Tools/XSStrike && sudo pip install -r requirements.txt && python2 xsstrike")
wait = input("Press [Enter] to go back...")
os.system("python3 DPredator.py")
