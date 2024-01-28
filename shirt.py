import sys
from os.path import splitext
from os import path
from PIL import Image, ImageOps


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else :
    pass

if (sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".jpeg")) and sys.argv[2].endswith(".png"):
    sys.exit("Input and output have different extensions")
elif (sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".jpeg")) and sys.argv[1].endswith(".png"):
    sys.exit("Input and output have different extensions")
else :
    pass

root_ext1 = splitext(sys.argv[1])
root_ext2 = splitext(sys.argv[2])
if (root_ext1[1] == ".jpg" or root_ext1[1] == ".png"
    or root_ext1[1] == ".jpeg") and (root_ext2[1] == ".jpg" or root_ext2[1] == ".png"
                                     or root_ext2[1] == ".jpeg"):
    pass
else :
    sys.exit("Invalid input")

if path.exists(sys.argv[1]) :
    if path.exists(sys.argv[2]):
        pass
    else :
        sys.exit("Invalid input")
else:
    sys.exit("Invalid input")

try:
    img = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Invalid input")

shirt = Image.open("shirt.png")
size = shirt.size
photo = ImageOps.fit(img, size, method=0, bleed=0.0, centering=(0.5, 0.5))
photo.paste(shirt, shirt)
photo.save(sys.argv[2])
