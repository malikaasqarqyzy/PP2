def count_lines_in_file(file_path):
    line_count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line_count += 1
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    return line_count

#example
file_path = 'C:\\Users\\PC\\Desktop\\Python pp2\\PP2\\file1.txt'
number_of_lines = count_lines_in_file(file_path)

if number_of_lines is not None:
    print(f"The file has {number_of_lines} lines.")