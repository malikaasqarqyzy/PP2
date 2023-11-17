import os

def check_path_and_split(path):
    if os.path.exists(path):
        directory, filename = os.path.split(path)
        return True, (directory, filename)
    else:
        return False, (None, None)

#example
path = r"C:\Users\PC\Desktop\Python pp2"
exists, (directory, filename) = check_path_and_split(path)

#results
if exists:
    print(f"Path exists. Directory: {directory}, Filename: {filename}")
else:
    print("Path does not exist.")