import sys
import os
import tabulate
import csv

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)


file_name = sys.argv[1]

if not file_name.endswith('.csv'):
    print("Not a CSV file")
    sys.exit(1)

if not os.path.isfile(file_name):
    print("File does not exist")
    sys.exit(1)

table_data = []
with open(file_name) as file:
    reader = csv.reader(file)
    for row in reader:
        table_data.append(row)

# Print the table using tabulate
print(tabulate.tabulate(table_data, headers="firstrow", tablefmt="grid"))
