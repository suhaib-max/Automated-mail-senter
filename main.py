import random
import smtplib
import datetime as td

email = "suhaibvbm@gmail.com"
password = "your_app_password"

# At a time and date
now = td.datetime.now()
# Today weekday
week = now.weekday()

if week == 6:
    with open("quates.txt","r") as data:
        content = data.readlines()
        quote = random.choice(content)


