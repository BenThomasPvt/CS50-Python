import sys
import random

# The documentation for pyfiglet isn’t very clear, but you can use the module as follows:
from pyfiglet import Figlet

figlet = Figlet()

# You can then get a list of available fonts with code like this:
# print(figlet.getFonts())

# You can set the font with code like this, wherein f is the font’s name as a str:
# figlet.setFont(font=f)

# And you can output text in that font with code like this, wherein s is that text as a str:
# print(figlet.renderText(s))


if len(sys.argv) == 1:
    # font not spectified
    figlet.setFont(font=random.choice(figlet.getFonts()))

elif len(sys.argv) == 3 and sys.argv[1] == '-f':
    # correct font specified
    font = sys.argv[2]
    if font in figlet.getFonts():
        figlet.setFont(font=font)
    else:
        print("Invalid usage")
        sys.exit(1)

else:
    print("Invalid usage")
    sys.exit(1)
text = input("Input: ")
print(figlet.renderText(text))
