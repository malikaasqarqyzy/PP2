from datetime import date, timedelta
#Write a Python program to print yesterday, today, tomorrow.

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today", today)
print("Tomorrow:", tomorrow)