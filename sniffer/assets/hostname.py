from scapy.all import socket
from sys import argv
from assets import ui

def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except socket.herror:
        return "Unknown"

if __name__ == "__main__":
    if len(argv) == 1:
        pass
    else:
        ui.clear()
        print(f"\n\nStart the program by runnning the app.py from the parent directory \n\n")
        input("Press Enter to continue ... ")
        ui.clear()