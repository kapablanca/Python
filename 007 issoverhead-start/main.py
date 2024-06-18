import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 38.108100  # Your latitude
MY_LONG = 23.763650  # Your longitude
my_email = "teststathovits@gmail.com"
password = "fxfqvghhdhxdhgsx"


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if ((MY_LAT + 5) >= iss_latitude >= (MY_LAT - 5)) and ((MY_LONG + 5) >= iss_longitude >= (MY_LONG - 5)):
        return True
    else:
        return False


# Your position is within +5 or -5 degrees of the ISS position.

def dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if sunrise <= time_now <= sunset:
        return False
    else:
        return True


while True:
    if iss_overhead() and dark():
        with smtplib.SMTP("gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="stathovits@hotmail.com",
                msg=f"Subject:ISS VISIBLE\n\n"
                    f"Look up, it's ISS!"
            )
    time.sleep(60)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
