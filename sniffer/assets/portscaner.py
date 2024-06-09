from scapy.all import sr1 , IP , TCP 
import json
from assets import ui
from sys import argv 

def NameChecker(port):
    with open("assets/cPorts.json","r") as file:
        data = json.load(file)
        if port in data:
            return f"{port} ----- {data[port]}"
        else:
            return f"{port} -----  is open but no name found " 

def port_scan(ip, ports):
    open_ports = []
    closed_ports = []
    open_ports_names = []
    for port in range(ports[0],ports[1]):
        response = sr1(IP(dst=ip) / TCP(dport=port, flags="S"), timeout=0.1, verbose=0)
        if response and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            open_ports.append(port)
            print(f"{port} is open")
        else:
            closed_ports.append(port)
            print(f"{port} is closed")
    ui.clear()
    ui.banner()
    # print("Open Ports are" , open_ports)
    for x in open_ports:
        data = NameChecker(str(x))
        open_ports_names.append(data)
    return open_ports,open_ports_names
            

def CommonPorts(ip):
    open_ports = []
    closed_ports = []
    open_port_name = []
    with open("assets/cPorts.json","r") as file:
        data = json.load(file)
        for x in data:
            port = int(x)
            response = sr1(IP(dst=ip) / TCP(dport=port, flags="S"), timeout=0.1, verbose=0)
            if response and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                open_ports.append(port)
                print(f"{port} is open")
            else:
                closed_ports.append(port)
                print(f"{port} is closed")
    ui.clear()
    ui.banner()
    for x in open_ports:
        data = NameChecker(str(x))
        open_port_name.append(data)
    return open_ports , open_port_name


if __name__ == "__main__":
    if len(argv) == 1:
        pass
    else:
        ui.clear()
        print(f"\n\nStart the program by runnning the app.py from the parent directory \n\n")
        input("Press Enter to continue ... ")
        ui.clear()