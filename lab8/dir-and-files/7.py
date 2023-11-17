def copy_file_contents(source_file, destination_file):
    with open(source_file, 'r') as src:
        contents = src.read()
    
    with open(destination_file, 'w') as dest:
        dest.write(contents)

copy_file_contents('source.txt', 'destination.txt')