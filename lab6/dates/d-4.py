from datetime import datetime
#Write a Python program to calculate two date difference in seconds.

def diff_in_sec(start_date, end_date):
    delta = end_date - start_date
    return delta.total_seconds()

#example:
date1 = datetime(2023, 1, 1, 12, 0, 0)
date2 = datetime(2023, 1, 2, 12, 0, 0)
diff = diff_in_sec(date1, date2)

print(f"Difference between {date1} and {date2} is {diff} seconds")