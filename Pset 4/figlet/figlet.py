from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
font = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in font:
            text = input("Input: ")
            my_font = figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(text))
        else :
            sys.exit("invalid second command-line argument")
    else:
        sys.exit("invalid first command-line argument")
elif len(sys.argv) == 1:
    text = input("Input: ")
    my_font = figlet.setFont(font=random.choice(font))
    print(figlet.renderText(text))
else:
    sys.exit("argument not true")
