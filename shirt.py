import sys
from os.path import splitext
from os import path
from PIL import Image, ImageOps
from sklearn.utils import resample


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else :
    pass

if sys.argv[1].endswith(".jpg") and sys.argv[2].endswith(".png"):
    sys.exit("Input and output have different extensions")
elif sys.argv[2].endswith(".jpg") and sys.argv[1].endswith(".png"):
    sys.exit("Input and output have different extensions")
else :
    pass

root_ext1 = splitext(sys.argv[1])
root_ext2 = splitext(sys.argv[2])
if (root_ext1[1] == ".jpg" or root_ext1[1] == ".png") and (root_ext2[1] == ".jpg" or root_ext2[1] == ".png"):
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

shirt = Image.open("shirt.png")
width = shirt.width
height = shirt.height
with Image.open(sys.argv[1]) as im:
    photo = ImageOps.fit(im, (width, height), method=0, bleed=0.0, centering=(2, 0.5))
    photo.paste(shirt, shirt)
    photo.save(sys.argv[2])
