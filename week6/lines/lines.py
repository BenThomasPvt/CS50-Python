import sys
import os

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)


file_name = sys.argv[1]

if not file_name.endswith('.py'):
    print("Not a Python file")
    sys.exit(1)

if not os.path.isfile(file_name):
    print("File does not exist")
    sys.exit(1)

count = 0

with open(file_name, 'r') as file:
    for line in file:
        stripped_line = line.strip()
        # Check if the line is not blank and not a comment
        if stripped_line and not stripped_line.startswith('#'):
            count += 1

print(count)
