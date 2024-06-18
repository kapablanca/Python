##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import pandas as pd
import random
import smtplib
import datetime as dt

my_email = "teststathovits@gmail.com"
password = "fxfqvghhdhxdhgsx"
change_name = "[NAME]"

df = pd.read_csv("birthdays.csv")
birthdays = df.to_dict(orient="records")

today = dt.datetime.now()
month = today.month
day = today.day

for entry in birthdays:
    if entry["month"] == month and entry["day"] == day:
        name = entry["name"]
        email = entry["email"]

        letter_text = f"letter_{random.randint(1,3)}.txt"
        with open(f"./letter_templates/{letter_text}") as file:
            letter = file.read()
        new_letter = letter.replace(change_name, name)

# Actually I don't need to write the file and read it and send it again. Just sae the replaced to a variable and use it.
        # with open(f"./letter_templates/new_letter_{name}.txt", "w") as file:
        #     file.write(new_letter)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            # with open(f"./letter_templates/new_letter_{name}.txt") as file:
            #     text_sending = file.read()
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Happy Birthday!\n\n"
                    f"{new_letter}"
            )
