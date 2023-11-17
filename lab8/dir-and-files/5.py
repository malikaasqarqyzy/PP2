def write_full_list_to_file(file_path, my_list):
    with open(file_path, 'w') as file:
        file.write(str(my_list))

#example
my_list = ['apple', 'banana', 'cherry']
file_path = 'C:\\Users\\PC\\Desktop\\Python pp2\\PP2\\file2.txt'
write_full_list_to_file(file_path, my_list)