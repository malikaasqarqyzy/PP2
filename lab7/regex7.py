import re
def camel_to_snake(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()

    text = re.sub('([a-z0-9])([A-Z])', r'\1_\2', text).lower()
    return text

filepath = 'C:\\Users\\PC\\Downloads\\row.txt'

converted_text = camel_to_snake(filepath)
print(converted_text)