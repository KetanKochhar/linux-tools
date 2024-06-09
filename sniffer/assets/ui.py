import os 
from pyfiglet import Figlet
from colorama import Fore , Back , Style , init
from sys import argv

def clear():
    OsName = os.name
    if OsName == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def banner():
    init()
    f = Figlet()
    f1 = Figlet()
    title = f.renderText("Network Sniffer")
    author = f1.renderText("Made By Ketan ")
    print(f"{Fore.GREEN} {title}")
    print(f"{author}")
    print(Style.RESET_ALL)

if __name__ == "__main__":
    if len(argv) == 1:
        pass
    else:
        clear()
        print(f"\n\nStart the program by runnning the app.py from the parent directory \n\n")
        input("Press Enter to continue ... ")
        clear()