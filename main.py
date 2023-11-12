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

    print(quote)
    #smtp= mail server provident it defulted to google gmail
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        #for the securing our data in encrpted
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,
                            to_addrs="suhaibvbm@gmail.com",
                            msg=f"Subject:Monday motivational quotes\n\n{quote}")
