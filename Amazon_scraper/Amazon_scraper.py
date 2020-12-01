# created on 01.12.2020 by dafr
#Program sends an email to myself if the price for ps4 controller drops below 50€

import requests
from time import sleep, strftime
from bs4 import BeautifulSoup
from selenium import webdriver
import smtplib

chromedriver_path = "C:/Users/dafr/Programming/Chromedriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_path) # This will open the Chrome window

URL ='https://www.amazon.de/PlayStation-DualShock-Wireless-Controller-schwarz/dp/B01GVQUX3U/ref=sr_1_3?__\
    mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=ps4+controller&qid=1606824403&sr=8-3'

def check_price():
    get = driver.get(URL)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')

    title = soup.find(id="productTitle")
    title = title.text.strip()

    price = soup.find('span',id="priceblock_ourprice")
    price = price.text.strip()
    price = price[:-2]
    price = float(price.replace(',', '.'))

    if price < 50:
        send_mail()
    
    # print(title)
    # print(price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('Insert_your_email', 'Insert_password')

    subject = "Hey Daniel, the price fell down"
    body = "Check the amazon link: https://www.amazon.de/PlayStation-DualShock-Wireless-Controller-schwarz/dp/B01GVQUX3U/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=ps4+controller&qid=1606824403&sr=8-3"
    
    msg = f"Subject: {subject}\n\n {body}"

    server.sendmail(
        "Insert_sending_email",
        "dafr@hotmail.de",
        msg
    )
    print("Email has been sent")

    server.quit()

check_price()