
import csv
import sys
import os
from tqdm import tqdm

sys.path.append("..")
import statkit as sk

def write_csv(file, data):
    with open(file, "w") as data_file:
        writer = csv.writer(data_file)
        writer.writerows(data)
    print(f"done saving {file}")

files = [i for i in os.listdir() if i != os.path.basename(__file__)]

for file in tqdm(files):
    data = list(csv.reader(open(file)))
    data = [sk.tokenize(i[-1]) + [i[0]] for i in tqdm(data)]
    write_csv(f"new-{file}", data)


