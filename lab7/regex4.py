import re
def regex4(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        match = re.findall('[A-Z]{1}.+[a-z]', content)
        return match

filepath = 'C:\\Users\\PC\\Downloads\\row.txt'
res = regex4(filepath)
print(res)