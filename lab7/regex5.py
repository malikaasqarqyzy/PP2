import re
def regex5(filepath):
    with open(filepath, 'r', encoding = 'utf-8') as file:
        content = file.read()
        match = re.search('a.*b$', content)
        if match:
            return match.group()
        else:
            return "No match found"

filepath = 'C:\\Users\\PC\\Downloads\\row.txt'
res = regex5(filepath)
print(res)