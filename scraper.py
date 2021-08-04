import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/New-Apple-Watch-GPS-40mm/dp/B08KGVJQC8/ref=sr_1_5?dchild=1&keywords=apple+watch+series+6&qid=1627926465&sr=8-5'

#headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36,'}
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64)', 'Cache-Control': 'no-cache', "Pragma": "no-cache"}

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')


    title = soup.find( id = "productTitle").get_text()
    price = soup.find( id = "priceblock_ourprice").get_text()
    converted_price_string = price[1:7]
    converted_price = float(converted_price_string.replace(',',''))

    if(converted_price < 350):
        send_mail()


    print(converted_price)
    print(title.strip(), price.strip())
    #print (soup)

    if(converted_price < 350):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('avillalobos.code', 
                 # 'password here'
                )

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.com/New-Apple-Watch-GPS-40mm/dp/B08KGVJQC8/ref=sr_1_5?dchild=1&keywords=apple+watch+series+6&qid=1627926465&sr=8-5'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'avillalobos.code@gmail.com',
        'angel_villalobos5@yahoo.com',
        msg

    )
    print('Email Sent out')

    server.quit()

check_price()
