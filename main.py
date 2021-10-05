import smtplib
import requests
from bs4 import BeautifulSoup
import time

while True:
    url = "https://coinmarketcap.com/currencies/eos/"

    html = requests.get(url)
    soup = BeautifulSoup(html.content)

    price = soup.find("div",{"class":"priceValue"})

    icerik = f"EOS Coin güncel değeri : {price.text}"  


    
    content = icerik
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("cansahiny.34@gmail.com","lx32971azx")
    mail.sendmail("cansahiny.34@gmail.com","cansahiny.34@gmail.com",content)

    time.sleep(3600)
    
