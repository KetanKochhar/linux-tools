from pyfiglet import Figlet
import os 
import requests
from bs4 import BeautifulSoup
import time

# Global list
AllWebsiteUrl = []
blacklist = []
headlist =[]

def clear():
    OsName = os.name
    if OsName == "nt":
        os.system("cls")
    else:
        os.system("clear")

def banner():
    f = Figlet()
    print(f.renderText("Web crawler"))
    print(f.renderText("Made by Ketan"))

def getunwated():
    with open("blacklist.txt","r") as f:
        data = f.readlines()
        # print(data)
        data =[line.rstrip('\n') for line in data]
        blacklist.extend(data)

def gethead():
    with open("headlist.txt","r") as f :
        data = f.readlines()
        data = [line.rstrip("\n") for line in data]
        # print(data)
        headlist.extend(data)

def get_head(url,headlist):
    res = requests.get(url)
    head = res.headers
    # print(head)
    if head in headlist:
        pass
    else:
        print(f"Missing {head} in the {url}")

def check_anchor_tag(WebsiteUrl , unwated):
    print("Started")
    res = requests.get(WebsiteUrl)
    html = res.text
    soup = BeautifulSoup(html,"html.parser")
    ATag = soup.findAll("a")
    for x in ATag:
        href = x.get("href")
        if href == None:
            pass
        elif not any (site in href for site in unwated):
            AllWebsiteUrl.append(href)
        else:
            pass
    print("Filtered",len(AllWebsiteUrl),"out of ",len(ATag))

def sub_links(WebsiteUrl,unwated):
    print(f"\nScaning {WebsiteUrl}")
    res = requests.get(WebsiteUrl)
    html = res.text
    soup = BeautifulSoup(html,"html.parser")
    ATag = soup.findAll("a")
    for x in ATag:
        link = x.get("href")
        if link in AllWebsiteUrl:
            # print("no Url Found")
            pass
        elif link == None:
            pass
        elif not any (site in link for site in unwated):
            AllWebsiteUrl.append(link)
            # print(link)
        else:
            pass


if __name__ == "__main__":
    clear()
    banner()
    getunwated()
    gethead()
    if headlist == []:
        print("Please specify the head that you need to check")
        print("exiting")
        quit()
    Url = input("Enter the website full including http/s : ")
    delay = input("press 1 to do with delay press enter to continue: ")
    if delay == "1":
        seconds = input("Enter the delay in the seconds : ")
        check_anchor_tag(Url,blacklist)
        print(f"Scaning {len(AllWebsiteUrl)}")
        for index , endpoint in enumerate(AllWebsiteUrl):
            print(f"Scaned {index + 1} out of {len(AllWebsiteUrl)}")
            print(f"delay of {seconds} seconds")
            url = f"{Url}/{endpoint}"
            sub_links(url,blacklist)
            time.sleep(int(seconds))
        clear()
        print("Getting the Head from this urls" ,len(AllWebsiteUrl))
        for sites in AllWebsiteUrl:
            link = f"{Url}/{sites}"
            get_head(link,headlist)
        input("Press enter to exit : ")
        clear()
    else:
        check_anchor_tag(Url,blacklist)
        print(f"Scaning {len(AllWebsiteUrl)}")
        for index , endpoint in enumerate(AllWebsiteUrl):
            print(f"Scaned {index + 1} out of {len(AllWebsiteUrl)}")
            url = f"{Url}/{endpoint}"
            sub_links(url,blacklist)
        clear()
        print("Getting the Head from this urls" ,len(AllWebsiteUrl))
        for sites in AllWebsiteUrl:
            link = f"{Url}/{sites}"
            get_head(link,headlist)
        input("Press enter to exit : ")
        clear()
