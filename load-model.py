
import pickle

# load the model
with open("model.pickle", "rb") as file:
    classifier = pickle.load(file)
    vectorizer = pickle.load(file)


#print(f"Enter text to classify:")
#while True:
#    text = input("> ")
#    prediction = classifier.predict([text])
#    print(f" sentiment: {prediction}")

# sample use
sample_tweets = [
    "Wow it is so cool",
    "this stuff is boring",
    "This will make you rich",
    "I don't care"
]

# report
predictions = classifier.predict(sample_tweets)
results = zip(sample_tweets, predictions)

def wrap(input_str, max_length=20):
    if len(input_str) <= max_length:
        return input_str
    else:
        return input_str[:max_length] + ".."

print("[Model Report]")
print(classifier.report)

print("[Model predictions]")
for index, result in enumerate(results, start=1):
    print(f"{'':<5}{index:<{len(str(len(predictions)))+2}} {wrap(result[0]):<25}{result[1]}")

