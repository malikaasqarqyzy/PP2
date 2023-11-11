import re
def split_on_uppercase(text):
    segments = re.split('(?=[A-Z])', text)
    return ' '.join(i for i in segments if i)

with open("C:\\Users\\PC\\Downloads\\row.txt", "r", encoding="utf-8") as file:
    text = file.read()

split_text = split_on_uppercase(text)
print(split_text)
