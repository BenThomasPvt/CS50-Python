import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

ifile = sys.argv[1]
ofile = sys.argv[2]

valid = ['.jpg', '.jpeg', '.png']

iex = os.path.splitext(ifile)[1].lower()
oex = os.path.splitext(ofile)[1].lower()

if iex not in valid or oex not in valid:
    print("Invalid input")
    sys.exit(1)

if iex != oex:
    print("Input and output have different extensions")
    sys.exit(1)


if not os.path.isfile(ifile):
    print("Input does not exist", ifile)
    sys.exit(1)

shirt = Image.open("shirt.png")
muppet = Image.open(ifile)
# shirt = shirt.resize(muppet.size, Image.LANCZOS)
muppet = ImageOps.fit(muppet, shirt.size)

if shirt.mode != 'RGBA':
    shirt = shirt.convert('RGBA')

# print(size)
muppet.paste(shirt, (0, 0), shirt)

muppet.save(ofile)
