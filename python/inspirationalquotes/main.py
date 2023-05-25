import smtplib
import datetime as dt
import random
my_email = "richardjamalthefifth@gmail.com"
password = "dqucmpllnxzbszop"
now = dt.datetime.now()
if now.weekday() == 2:
    with open("inspirationalquotes/quotes.txt", "r") as file:
        lines = file.readlines()
        quote = random.choice(lines)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="darwinnextup@yahoo.com",
            msg=f"Subject:Inspirational Quote\n\n{quote}")
