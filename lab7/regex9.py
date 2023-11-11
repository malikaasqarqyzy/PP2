import re
def insert_spaces(text):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

with open("C:\\Users\\PC\\Downloads\\row.txt", "r", encoding="utf-8") as file:
    text = file.read()

formatted_text = insert_spaces(text)
print(formatted_text)