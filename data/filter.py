
import csv
import sys
from tqdm import tqdm

sys.path.append("../")
import statkit as sk

data = list(csv.reader(open("dataset.csv")))
data = [sk.tokenize(i[-2])+[i[2]] for i in tqdm(data)]

def filter(data):
    data = [i[:-1]+[1] if i[-1] == "5" else \
            i[:-1]+[-1] if i[-1] == "2" else \
            i[:-1]+[0] for i in data
    ]
    return data

data = filter(data)
sk.to_csv("product-sentiment.csv", data)

