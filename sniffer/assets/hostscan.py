from scapy.all import Ether , srp , ARP
from assets import hostname , ui
from sys import argv

UpHost = []
downhost = []
res = []
def arp_scan(ip):
    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    ans, unans = srp(request, timeout=0.5, retry=1,verbose=0)
    result = []

    for sent, received in ans:
        mac = received.hwsrc
        name = hostname.get_hostname(received.psrc)
        result.append({'IP': received.psrc, 'MAC': mac, 'name': name})

    if result == []:
        print("Host is Down for", ip)
        downhost.append(ip)
    else:
        UpHost.append(ip)
        res.append(result)
        print(result[0])
    
    # ui.clear()
    return UpHost , downhost , res

if __name__ == "__main__":
    if len(argv) == 1:
        pass
    else:
        ui.clear()
        print(f"\n\nStart the program by runnning the app.py from the parent directory \n\n")
        input("Press Enter to continue ... ")
        ui.clear()