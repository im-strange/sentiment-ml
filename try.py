"""
import pandas as pd

df = pd.read_csv("tweets.csv", encoding="latin-1")
df = df.drop(columns=["date", "id", "q", "username"])

sample = df.groupby("label").apply(lambda x: x.sample(200000, random_state=42))
sample = sample.reset_index(drop=True)
sample.to_csv("data.csv", index=False)
"""
import csv

data = list(csv.reader(open("reviews.csv")))
data = [i[:-1]+[5] if i[-1].lower() == "positive" else \
        i[:-1]+[2] if i[-1].lower() == "negative" else \
        i[:-1]+[3] for i in data]

with open("main-reviews.csv","w") as file:
     writer = csv.writer(file)
     writer.writerows(data)
