
import pickle
from model import SentimentClassifier

classifier = SentimentClassifier()
vectorizer = classifier.vectorizer

with open("model.pickle", "wb") as file:
    pickle.dump(classifier, file)
    pickle.dump(vectorizer, file)

print("model saved!")
