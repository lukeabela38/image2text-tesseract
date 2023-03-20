import os
import cv2
import pytesseract
import statistics
#from postprocessing import *

INPUT_PATH = "input/"
OUTPUT_PATH = "output/"
CONFIG = "--psm 6 --oem 1"

def pipeline(file):

    img = cv2.imread(INPUT_PATH + file)
    text = pytesseract.image_to_string(img, config=CONFIG)

    iterator = file.split(".")[0]
    with open(OUTPUT_PATH + f"{iterator}.txt", 'w') as f:
        f.write(text)

    cv2.imwrite(OUTPUT_PATH + f"{iterator}.jpg", img)

    return text

def main():

    files = os.listdir(INPUT_PATH)
    print(len(files))

    for file in files:
        pipeline(file)


if __name__ == "__main__":
    main()
