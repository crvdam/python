import sys, os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

ext1 = os.path.splitext(sys.argv[1].lower())
ext2 = os.path.splitext(sys.argv[2].lower())

if ext1[1] != ext2[1]:
    sys.exit("Input and output have different extensions")
elif ".jpg" != ext1[1] and ".jpeg" != ext1[1] and ".png" != ext1[1]:
    sys.exit("Invalid input")

try:
    img = Image.open(sys.argv[1])
    shirt =  Image.open("shirt.png")
    img = ImageOps.fit(img, shirt.size)
    img.paste(shirt, shirt)
    img.save(sys.argv[2])


except FileNotFoundError:
    sys.exit("Invalid input")