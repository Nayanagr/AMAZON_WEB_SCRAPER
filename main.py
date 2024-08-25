import os
import smtplib
import requests
from bs4 import BeautifulSoup
# -----------------------------------------CONSTANTS-------------------------------------------------------------------#
header = {
    "User-Agent" : "Defined",

}
URL = 'https://www.amazon.in/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/'

password = os.environ.get("PASSWORD")
MY_EMAIL = os.environ.get("EMAIL")
TARGET_PRICE = 8999.00

# ---------------------------------------COMM WITH API ---------------------------------------------------------------#
response = requests.get(url=URL, headers=header).text

data = response
soup = BeautifulSoup(data, features="lxml")
price = float(soup.find("input",{"id":"priceValue"}).get("value"))

# VALUE CHECK AND SENDING EMAIL
send_email = False

if price <= TARGET_PRICE:
    send_email = True

if send_email:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="nayanforudemy@gmail.com", password=password)
        connection.sendmail(from_addr="nayanforudemy@gmail.com", to_addrs=MY_EMAIL, msg=f"subject:AMAZON PRICE ALERT🚨🚨\n\n The price for the product has reached the Taget Price of {TARGET_PRICE}, buy now {URL} ".encode("utf8"))

