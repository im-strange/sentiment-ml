
import csv
import statkit as sk
from tqdm import tqdm

def filter(file):
    data = list(csv.reader(open(file, encoding="latin-1")))[1:]
    data = [[sublist[-1]] + [sublist[0]] for sublist in tqdm(data)]
    return data

def write_csv(file, data):
    with open(file, "w") as data_file:
        writer = csv.writer(data_file)
        writer.writerows(data)
    print(f"done saving {file}")


data = list(csv.reader(open("tweets-02.csv", encoding="latin-1")))
chunk = 150000

ctr = 1

for i in tqdm(range(0, len(data), chunk)):
    filename = f"data-0{ctr}.csv"
    write_csv(filename, data[i:i+chunk])
    print(f"done writing -> {filename}")
    ctr += 1

"""
pos = 4
neg = 2

new = []

for i in tqdm(data):
    label = ""
    if int(i[-1]) >= pos:
        label = "positive"
    elif int(i[-1]) <= neg:
        label = "negative"
    else:
        label = "neutral"

    new.append(i[:-1]+[label])

write_csv("cleaned.csv", new)
"""
