import re
def regex3(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        match = re.search('[a-z]+_[a-z]+', content)
        return match

filepath = 'C:\\Users\\PC\\Downloads\\row.txt'
res = regex3(filepath)
print(res)