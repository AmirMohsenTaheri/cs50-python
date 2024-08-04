from PIL import Image
from PIL import ImageOps

import sys

def main():
    if len(sys.argv) == 3:
        if recognition(sys.argv[1], sys.argv[2]):
            try:
                mask = Image.open("shirt.png")
                shirt = Image.open(sys.argv[1])
                size = mask.size
                shirt = ImageOps.fit(shirt, size)
                shirt.paste(mask, mask= mask)
                shirt.save(
                    sys.argv[2], format=None
                )



            except(FileNotFoundError):
                sys.exit("Could not find files")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    else:
        sys.exit("Too many command-line arguments")


def recognition(x,y):
    first_file = x.split(".")
    second_file = y.split(".")
    if first_file[1] == second_file[1]:
        match first_file[1]:
            case "jpg" | "jpeg" | "png":
                return True
            case _ :
                sys.exit("Invalid input ")
    else:
        sys.exit("Input and output have different extensions")

main()
