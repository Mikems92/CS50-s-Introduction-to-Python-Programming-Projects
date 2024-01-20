import random
import sys
from pyfiglet import Figlet

input = input("Input :")
figlet = Figlet()
if len(sys.argv) == 1:
    random_font = random.choice(figlet.getFonts())
    figlet.setFont(font=random_font)
    print(figlet.renderText(input))
elif len(sys.argv) == 2:
    sys.exit("Invalid usage")
elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")
        elif sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in figlet.getFonts():
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(input))
        elif sys.argv[1] != "-f" or sys.argv[1] != "--font" or sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")


