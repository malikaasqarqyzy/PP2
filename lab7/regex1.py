import re
def regex1(filepath):
    with open(filepath, 'r', encoding = 'utf-8') as file:
        content = file.read()
        matches = re.findall('ab*', content)
        return matches

filepath = 'C:\\Users\\PC\\Downloads\\row.txt'
res = regex1(filepath)
print(res)