
import pickle

# load the model
with open("model.pickle", "rb") as file:
    print(f"[+] loading model..")
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
    "I don't care",
    "this is fascinating",
    "this world is dumb",
    "you are dumb"
]

# report
predictions = classifier.predict(sample_tweets)
results = list(zip(sample_tweets, predictions))

def wrap(input_str, max_length=20):
    if len(input_str) <= max_length:
        return input_str
    else:
        return input_str[:max_length] + ".."

print("[Model Report]")
print(classifier.report)

print("[Model predictions]")
for text, result in results:
    y = 25 if int(result[0]) not in [1,0] else 26
    x = 12 if int(result[0]) not in [1,0] else 11
    wrapped = wrap(text)
    predicted_class = result[0]
    class_prob = list(map((lambda x: round(x, 3)),result[1]))

    print(f"{'':<3}{wrapped:<{y}}{predicted_class:<{x}}{class_prob}")
