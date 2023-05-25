import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "https://www.amazon.com/Nutricost-Creatine-Monohydrate-Micronized-Powder/dp/B01EVVQX9U/ref=sr_1_1_sspa?crid=1A9Y1EZLI1IL8&keywords=creatine+1kg&qid=1684942985&sprefix=creatine+1k%2Caps%2C159&sr=8-1-spons&psc=1&smid=A2YD2H3KGK1F4L&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE5SkZTUUY4Q0ZCS1AmZW5jcnlwdGVkSWQ9QTAzMzAxNzk1MTVaQzdINFo3TzcmZW5jcnlwdGVkQWRJZD1BMDczMjA5MlMxWTFBR0k4UEZTOSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language" : "en-US,en;q=0.9",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding" : "gzip, deflate, br"
}
buy_price = 45.00
response = requests.get(URL, headers=headers)
response.raise_for_status()
amazon_site_html = response.text
soup = BeautifulSoup(amazon_site_html, "lxml")
price_tag = soup.find(name="span", class_="a-offscreen")
title_tag = soup.select("#productTitle")[0]
title = title_tag.getText().strip()
price = float(price_tag.getText().split("$")[1])


if price < buy_price:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("richardjamalthefifth@gmail.com", "dqucmpllnxzbszop")
        connection.sendmail(
            from_addr="richardjamalthefifth@gmail.com",
            to_addrs="darwinnextup@yahoo.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )