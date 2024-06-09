from assets import ui 
from sys import argv

def help():
    with open("assets/help.txt" , "r") as file :
        data = file.read()
        return data

if __name__ == "__main__":
    if len(argv) == 1:
        pass
    else:
        ui.clear()
        print(f"\n\nStart the program by runnning the app.py from the parent directory \n\n")
        input("Press Enter to continue ... ")
        ui.clear()