import re
def snake_to_camel(snake_string):
    camel_string = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), snake_string)
    return camel_string

with open("C:\\Users\\PC\\Downloads\\row.txt", "r", encoding="utf-8") as file:
    text = file.read()

camel_case_text = snake_to_camel(text)
print(camel_case_text)