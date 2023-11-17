import os

def check_path_access(path):
    access_info = {
        'exists': os.path.exists(path),
        'readable': os.access(path, os.R_OK),
        'writable': os.access(path, os.W_OK),
        'executable': os.access(path, os.X_OK)
    }
    return access_info

#example
path = r"C:\Users\PC\Desktop\Python pp2"
access_info = check_path_access(path)

#results
for key, value in access_info.items():
    print(f"{key.capitalize()}: {value}")