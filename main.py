import random
import smtplib
import datetime as td

# At a time and date
now = td.datetime.now()
# Today weekday
week = now.weekday()

if week == 6:
    with open("quates.txt","r") as data:
        content = data.readlines()
        
