try:
    with open("sample.txt", 'r') as file1:
        line1 = file1.readline()
        line2 = file1.readline()
        print(f"Line1: {line1}")
        print(f"Line2: {line2}")
except FileNotFoundError:
    print(f"Error: The file 'sample.txt' was not found")