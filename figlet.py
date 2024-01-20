import random
import sys
from pyfiglet import Figlet

input = input("Input :")
figlet = Figlet()
if len(sys.argv) == 1:
    random_font = random.choice(figlet.getFonts())
    figlet.setFont(font=random_font)
    print(figlet.renderText(input))
elif len(sys.argv) == 3:
    for font in figlet.getFonts():
        if sys.argv[1] == "-f" or sys.argv[1] == "--font" or sys.argv[2] == font:
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(input))
        else:
            sys.exit("Invalid usage")

