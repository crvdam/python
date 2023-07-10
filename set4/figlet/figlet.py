import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 3 and sys.argv[1] != "-f" and sys.argv[1] != "--font":
    sys.exit("Invalid usage")
elif len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid usage")

if len(sys.argv) == 1:
    f = random.choice(fonts)
else:
    f = sys.argv[2]

figlet.setFont(font=f)

s = input("Input: ")
print("Output: ")
print(figlet.renderText(s))