from datetime import datetime
#Write a Python program to drop microseconds from datetime.

def drop_micrsec(dt):
    return dt.replace(microsecond = 0)

#print(datetime.now())
print(drop_micrsec(datetime.now()))