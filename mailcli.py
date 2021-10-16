import argparse
from datetime import date

# import time
import requests

today = date.today()
weekday = date.weekday(today)
# print(weekday)
days = {
    "0": "Monday",
    "1": "Tuesday",
    "2": "Wednesday",
    "4": "Thursday",
    "4": "Friday",
    "5": "Saturday",
    "6": "Sunday",
}
day = days.get(str(weekday))
print(day)
print("\n")

url = "http://www.google.com"
#timeout = 5
try:
    request = requests.get(url, timeout=timeout)
    print("You're Connected to the Internet\n")
except (requests.ConnectionError, requests.Timeout) as exception:
    print("No internet connection.")


parser = argparse.ArgumentParser()
parser.add_argument("Name", type=str, help="Name of the Engineer in shift")
parser.add_argument("Day", type=str, help="Nmae of the weekday: Mon, Tue, Wed,...")
parser.add_argument("-v", "--verbosity", action="count", default=0)

args = parser.parse_args()

print(f"Your are Engineer {args.Name} and today is  {args.Day}", f"date: {today}\n")
print("Do you want to Draft or Send Directly? \nyes: 'y' \nor \nNo: 'n' ")
