import string

def generate_alphabet_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is the file for letter {letter}")

generate_alphabet_files()