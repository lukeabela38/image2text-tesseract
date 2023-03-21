import os
import re
import csv
import statistics
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from tqdm import tqdm

TARGET = "text_real/"
RESULT = "text_pred_control/"
HEADER = ["INDEX, TARGET, RESULT, COSINE SIMILARITY SCORE"]
CSVPATH = "results_docentr.csv"

def normalize(text):
    return text

vectorizer = TfidfVectorizer(tokenizer=normalize)

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

def readtext(path):

    try:
        with open(path, "rb") as f:
            return f.readlines()[0].decode("utf-8")
    except:
        return ""


def main():

    target_files = os.listdir(TARGET)
    target_files.sort()

    scores = []

    with open(CSVPATH, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(HEADER)

        for i, data in tqdm(enumerate(target_files)):

            target_text = readtext(f"{TARGET}{data}")
            target_text = re.sub(r'[^\w\s]', '', target_text)

            data = f"{data[:-5]}{int(data[-5]) * 2}.txt"
            result_text = readtext(f"{RESULT}{data}")
            result_text = re.sub(r'[^\w\s]', '', result_text)

            score = cosine_sim(target_text, result_text)
            #print(i, target_text, result_text, score)
            scores.append(score)
            writer.writerow([i, target_text, result_text, score])

    print("Mean of the sample is ", (statistics.mean(scores))) 
    print("Standard Deviation of the sample is ", (statistics.stdev(scores)))

if __name__ == "__main__":
    main()