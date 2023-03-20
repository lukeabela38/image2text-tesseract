import os
import cv2
import pytesseract
import numpy as np
from tqdm import tqdm

INPUT_PATH: str = "inputs_control/"
OUTPUT_PATH: str = "text_pred/"
CONFIG: str = "--psm 6 --oem 1"

def pipeline(file) -> str:

    path: str = f"{INPUT_PATH}{file}"
    img: np.ndarray = cv2.imread(path)
    text: str = pytesseract.image_to_string(img, config=CONFIG)

    iterator: str = file.split(".")[0]
    with open(OUTPUT_PATH + f"{iterator}.txt", 'w') as f:
        f.write(text)

    return text

def main() -> int:

    files = os.listdir(INPUT_PATH)

    for file in tqdm(files):
        pipeline(file)

    return 0


if __name__ == "__main__":
    main()
