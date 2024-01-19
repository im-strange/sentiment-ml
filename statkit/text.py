
import csv
import re
import os

#stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

module_dir = os.path.dirname(os.path.abspath(__file__))
stopwords_path = os.path.join(module_dir, "stopwords.csv")

with open(stopwords_path) as file:
    stopwords = list(csv.reader(file))
    stopwords = [i for sublist in stopwords for i in sublist]

# clean extra character(s) from a string
def clean_text(text):
    cleaned_text = re.sub(r'[^A-Za-z\s]', '', text)
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text

# tokenize a string
def tokenize(sentence):
    sentence = clean_text(sentence)
    words = re.findall(r"\b\w+\b", sentence.lower())
    return [word for word in words if word not in stopwords]

# get frequencies
def freq(list):
    freq = {}
    for word in list:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    return freq

# get keywords from a document
def fetch_keywords(document):
    freq = {}
    filtered = [clean_text(i[0]) for i in document]
    for sentence in filtered:
        for word in tokenize(sentence):
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
    keywords = list(sorted(freq.items(), key=lambda x: x[1], reverse=True))
    top_keywords = [i[0] for i in keywords]
    return top_keywords
