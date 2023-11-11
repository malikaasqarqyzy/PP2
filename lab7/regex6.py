import re
def find_match(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        match = re.sub("[ ,.]", ':', content)
        return match

filepath = 'C:\\Users\\PC\\Downloads\\row.txt'
res = find_match(filepath)
print(res)