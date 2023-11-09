import re

def find_match(text):
    with open('C:\\Users\\PC\\Downloads\\row.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        match = re.sub("[ ,.]", ':', text)
        return match

text = 'C:\\Users\\PC\\Downloads\\row.txt'
matches = find_match(text)
print(matches)