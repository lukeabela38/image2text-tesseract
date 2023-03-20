import os
import re
import csv
import statistics
from sklearn.feature_extraction.text import TfidfVectorizer

TARGET = "/workspace/text/"
RESULT = "/workspace/result/"
HEADER = ["INDEX, TARGET, RESULT, COSINE SIMILARITY SCORE"]
CSVPATH = "/workspace/results.csv"

def normalize(text):
    return text

vectorizer = TfidfVectorizer(tokenizer=normalize)

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

def readtext(path):

    with open(path) as f:
        lines = f.readlines()

    return lines

def main():

    target_files = os.listdir(TARGET)
    target_files.sort()

    scores = []

    with open(CSVPATH, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(HEADER)

        for i, data in enumerate(target_files):
            target_text = readtext(TARGET + data)[0]
            target_text = re.sub(r'[^\w\s]', '', target_text)

            result_text = readtext(RESULT + data)
            result_text = " ".join("".join(result_text).splitlines())
            result_text = re.sub(r'[^\w\s]', '', result_text)
            result_text = re.sub(' +', ' ', result_text)

            score = cosine_sim(target_text, result_text)
            print(i, target_text, result_text, score)
            scores.append(score)
            writer.writerow([i, target_text, result_text, score])

    print("Mean of the sample is ", (statistics.mean(scores))) 
    print("Standard Deviation of the sample is ", (statistics.stdev(scores)))

if __name__ == "__main__":
    main()