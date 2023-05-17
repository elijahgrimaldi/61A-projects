##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import pandas as pd
import smtplib
import datetime as dt
import random

my_email = "richardjamalthefifth@gmail.com"
password = "dqucmpllnxzbszop"
now = dt.datetime.now()
data = pd.read_csv("birthdayletter/birthdays.csv")
birthdays_dict = {(row.month,row.day): row for (index, row) in data.iterrows()}
print(birthdays_dict)
if (now.month,now.day) in birthdays_dict:
    birthday_person = birthdays_dict[(now.month,now.day)]
    to_email = birthday_person["email"]
    file_path = f"birthdayletter/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path, "r") as file:
        content = file.read()
    replaced_content = content.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:Happy Birthday!\n\n{replaced_content}")


