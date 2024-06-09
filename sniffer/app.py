import assets
import assets.help as help
import assets.hostname as hostname
import assets.hostscan as hostscan
import assets.portscaner as portscanner
import assets.ui as ui 

def main_menu():
    ui.clear()
    ui.banner()
    print("1. Scan Devices on local network ")
    print("2. IP Information (Name of the device) ")
    print("3. Open Port Scaner ")
    print("4. Name of host (by IP) ")
    print("5. Help ")
    print("6. Exit ")

def SubMenuOne():
    ui.clear()
    ui.banner()
    target = input("Enter the first 3 network bit to be scaned locally \n example 192.168.1.1 will be 192.168.1 \n : ")
    user = int(input("Enter the last IP to be scanned max is 255 : "))
    for IP in range(1,user+1):
        internet = f"{target}.{IP}"
        UpHost , DownHost , Result = hostscan.arp_scan(internet)
        print(f"{target}.{IP}")
    return UpHost , DownHost , Result
        

if __name__ == "__main__": 
    while True:
        ui.clear()
        ui.banner()
        main_menu()
        MainMenuChoice = input("Enter your choice (1-6) : ")
        if MainMenuChoice == "1":
            up , down , res = SubMenuOne()
            input("Press Enter to continue")
            ui.clear()
            ui.banner()
            print("1. Active Host")
            print("2. Down Host")
            print("3. All Information")
            print("4. Exit")
            us_ch = input("Enter your choice (1-4) : ")
            if us_ch == "1":
                print(up)
            elif us_ch== "2":
                print(down)
            elif us_ch== "3":
                for x in res:
                    print(x)
            elif us_ch== "4":
                pass
            else:
                print("Invalid Choice try again")
                pass
            input("Press Enter to continue")

        elif MainMenuChoice == "2":
            ui.clear()
            ui.banner()
            Target = input("Enter the IP to get the information : ")
            if len(Target) > 15:
                print("Invalid IP ")
                pass
            else:
                up , down , response = hostscan.arp_scan(Target)
                ui.clear()
                ui.banner()
                if response == []:
                    print("Try Again in some time ....")
                else:
                    print("\n\n" ,response[-1][0]["IP"],"\n\n",response[-1][0]["MAC"],"\n\n",response[-1][0]["name"],"\n\n")
            input("Press Enter to continue")
        elif MainMenuChoice == "3":
            ui.clear()
            ui.banner()
            target = input("Enter the target ip or doamin name : ")
            ui.clear()
            ui.banner()
            print("Select the scan type : ")
            print("1.Comman Ports scan ")
            print("2.Full Ports scan ")
            print("3.Custom Ports scan ")
            print("4.Exit ")
            us_ch = input("Enter your choice (1-4) : ")
            if us_ch == "1":    
                ports , Names = portscanner.CommonPorts(target)
                ui.clear()
                ui.banner()
                print(f"Found {len(ports)} open ports from {target}\n\n")
                for x in Names:
                    print(x)
            elif us_ch == "2":
                print("This may take a little time....")
                ports , name = portscanner.port_scan(target,[0,65535])
                ui.clear()
                ui.banner()
                for x in name:
                    print(x)
            elif us_ch =="3":
                ui.clear()
                ui.banner()
                print(f"Custom port scan for {target}")
                start = int(input("Enter the port to start the sacn : "))
                end = int(input("Enter the port to end the scan : "))
                print(f"Scaning{(end - start)+1} ports in total ")
                port , name = portscanner.port_scan(target,[start,end])
                ui.clear()
                ui.banner()
                print(f"Found {len(port)} open ports from {target}\n\n")
                for x in name:
                    print(x)
            elif us_ch == "4":
                pass
            else:
                print("invaild input try again")
                pass
            input("Press Enter to continue")
        elif MainMenuChoice == "4":
            ui.clear()
            ui.banner()
            target = input("Enter the ip to check the host name works only in local network : ")
            data = hostname.get_hostname(target)
            ui.clear()
            ui.banner()
            print(f"  Name associsted with {target} is {data}")
            input("Press Enter to continue")
        elif MainMenuChoice == "5":
            ui.clear()
            data = help.help()
            print(data)
            input("Press Enter to continue")
        elif MainMenuChoice == "6":
            ui.clear()
            break 
        else:
            print("invalid input try again")
            input("Press Enter to continue")
