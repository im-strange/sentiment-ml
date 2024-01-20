
import csv
import os
from tqdm import tqdm

files = [i for i in os.listdir() if i not in ["filter.py", "reviews-06.csv"]]
data = []
for file in tqdm(files):
    x = list(csv.reader(open(file)))[1:]
    for i in x:
        data.append(i)

pos = [i for i in data if int(i[-1]) >= 4]
neg = [i for i in data if int(i[-1]) <= 2]
neu = [i for i in data if int(i[-1]) == 3]

shortest = len(min(pos, neg, neu))

pos = pos[:shortest]
neg = neg[:shortest]
neu = neu[:shortest]

data = pos + neg + neu

with open("main.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(data)
