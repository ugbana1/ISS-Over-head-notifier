import requests
from datetime import datetime
import smtplib
MY_LAT = 6.41423 # Your latitude
MY_LONG = 7.516523 # Your longitude
EMAIL="youremail@gmail.com" #Use your email
PASSWORD ="ecfkhkyagxxxxfcn" #Use your pass word

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def my_issposition():
    if iss_latitude == MY_LAT +5 or  iss_latitude == MY_LAT-5:
        return True
    elif iss_longitude ==MY_LONG + 5 or iss_longitude ==MY_LONG -5:
        return True
    return False



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
my_issposition()

if my_issposition() ==True and sunset == time_now:
    connection =smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=EMAIL,password=PASSWORD)
    connection.sendmail(from_addr=EMAIL,to_addrs="okekeisaacs@gmail.com",msg="Subject:ISSPOSITION\n\nLook Up!")
else:
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=EMAIL,password=PASSWORD)
    connection.sendmail(from_addr=EMAIL,to_addrs="okekeisaacs@gmail.com",msg="Subject:ISSPOSITION\n\n Wait for it!")





