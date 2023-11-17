import os

def list_directories_files(path):
    directories = []
    files = []
    all_contents = []

    for root, dirs, files_in_dir in os.walk(path):
        for dir in dirs:
            directories.append(os.path.join(root, dir))
        for file in files_in_dir:
            files.append(os.path.join(root, file))
        break

    all_contents = directories + files
    return directories, files, all_contents

path = 'C:\\Users\\PC\\Desktop\\Python pp2\\PP2'
directories, files, all_contents = list_directories_files(path)

print("Directories:", directories)
print("Files:", files)
print("All Contents:", all_contents)