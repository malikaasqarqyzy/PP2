import os

def delete_file_if_exists(file_path):
    if os.path.exists(file_path) and os.access(file_path, os.W_OK):
        try:
            os.remove(file_path)
            print(f"File {file_path} has been deleted.")
        except OSError as e:
            print(f"Error: {e}")
    else:
        print("File does not exist or is not accessible.")

delete_file_if_exists('file_to_delete.txt')