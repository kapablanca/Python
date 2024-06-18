# import smtplib
#
# my_email = "teststathovits@gmail.com"
# password = "fxfqvghhdhxdhgsx"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="stathovits@hotmail.com", msg="Hello")

import datetime as dt
import random
import smtplib

my_email = "teststathovits@gmail.com"
password = "fxfqvghhdhxdhgsx"

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()

# print(day_of_the_week)
#
# date_of_birth = dt.datetime(year=1995, month=2, day=15)
# print(date_of_birth)
print(day_of_the_week)

if day_of_the_week == 6:
    with open("quotes.txt") as text:
        quotes = text.readlines()
        random_quote = random.choice(quotes)

    print(random_quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="stathovits@hotmail.com,",
            msg=f"Subject:Be Positive\n\n"
                f"{random_quote}"
        )
