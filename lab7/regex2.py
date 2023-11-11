import re
def regex2(filepath):
    with open(filepath, 'r', encoding = 'utf-8') as file:
        content = file.read()
        matches = re.search('ab{2}|b{3}', content)
        return matches

filepath = 'C:\\Users\\PC\\Downloads\\row.txt'
res = regex2(filepath)
print(res.group())