
import re
import os
import csv
from tqdm import tqdm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# +=

data1 = list(csv.reader(open("data/finance-sentiment.csv")))
data2 = list(csv.reader(open("data/reviews-sentiment.csv")))
data3 = list(csv.reader(open("data/movie-sentiment.csv")))
data4 = list(csv.reader(open("data/product-sentiment.csv")))

data = data4

class SentimentClassifier:
    def __init__(self, data=data):
        self.data = data
        self.alpha = 1
        self.data_text = [" ".join(row[:-1]) for row in self.data]
        self.data_labels = [row[-1] for row in self.data]

        self.X_train, self.X_test, self.Y_train, self.Y_test = None, None, None, None
        self.vectorizer = None
        self.model = None

        self.accuracy = None
        self.confusion_mat = None
        self.report = None

        # split data into training and testing set
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(
            self.data_text,
            self.data_labels
        )

        self.vectorizer = CountVectorizer()
        self.X_train = self.vectorizer.fit_transform(self.X_train)
        self.X_test = self.vectorizer.transform(self.X_test)

        # initialize a model
        self.model = MultinomialNB()
        self.model.fit(self.X_train, self.Y_train)

        # make a predictions with testing set
        predictions = self.model.predict(self.X_test)

        # get the prediction info
        self.accuracy = accuracy_score(self.Y_test, predictions)
        self.confusion_mat = confusion_matrix(self.Y_test, predictions)
        self.report = classification_report(self.Y_test, predictions)

    def test(self, data, labels):
        data = self.vectorizer.transform(data)
        predictions = self.model.predict(data)

        # get the prediction info
        report = classification_report(
            labels,
            predictions,
            zero_division = 0
        )

        print(report)

    def predict(self, data):
        data = self.vectorizer.transform(data)
        predicted = self.model.predict(data)
        prob = self.model.predict_proba(data)
        return list(zip(predicted, prob))

if __name__ == "__main__":
    #data = [i for i in list(csv.reader(open("data/data-01.csv")))[1:]]
    #x = [" ".join(i[:-1]) for i in data]
    #y = [i[-1].lower() for i in data]

    model = SentimentClassifier()
    print(model.report)
