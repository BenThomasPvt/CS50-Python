import sys
import os
import csv

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

ifile = sys.argv[1]
ofile = sys.argv[2]

if not ifile.endswith('.csv'):
    print("Not a CSV file")
    sys.exit(1)

if not os.path.isfile(ifile):
    print("Could not read", ifile)
    sys.exit(1)

with open(ifile, mode='r', newline='', encoding='utf-8') as infile, \
        open(ofile, mode='w', newline='', encoding='utf-8') as outfile:

    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])

    # Write the header to the output file
    writer.writeheader()

    # Process each row in the input file
    for row in reader:
        full_name = row['name']
        house = row['house']

        # Split the name into first and last
        last_name, first_name = (full_name.split(',')[0].strip(), full_name.split(',')[1].strip())


        # Write to the output file
        writer.writerow({"first": first_name, "last": last_name, "house": house})
