# --- Writing with 'with' ---

try:
    with open('output.txt', 'w') as f:
        f.write(input("Enter text to write to the file: "))
    print(f"Data sucessfully written to output.txt.")

except IOError as e:
    print(f"Error writing to file: {e}")

# --- Reading data with 'with' ---

# try:
#     with open('output.txt', 'r') as f:
#         for line in f:
#             print(line)
# except FileNotFoundError:
#     print("Error: output.txt not found.")
# except IOError as e:
#     print("Error reading from file", e)

# --- Appending data with 'with' ---

try:
    with open('output.txt', 'a') as f:
        f.write("\n--- Added later ---\n")
        f.write(input("Enter additional text to append: "))
    print("Data successfully appende.")
except IOError as e:
    print(f"Error appending to file: {e}")

# Verify appended content

print("Final content of output.txt:")

try:
    with open('output.txt', 'r') as f:
        for line in f:
            print(line)
except FileNotFoundError:
    print("Error: output.txt not found")