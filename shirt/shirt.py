import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_input()
    try:
        anh = Image.open(sys.argv[1])
    except:
        sys.exit("Input does not exist")

    ao = Image.open("shirt.png")
    kc = shirt.size
    cs = ImageOps.fit(anh, kc)
    cs.paste(ao, ao)
    cs.save(sys.argv[2])


def check_input():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arfuments")
    file1 = sys.argv[1].splitext()
    file2 = sys.argv[2].splitext()
    d1 = file1[1]
    d2 = file2[1]
    if check_duoi(d1) == False or check_duoi(d2) == False:
        sys.exit("Invalid input")
    if d1 != d2:
        sys.exit("Input and output have different extensions")


def check_duoi(duoi):
    if duoi in [".jpg", ".jpeg", ".png"]:
        return True
    return False

if __name__ == "__main__":
    main()
