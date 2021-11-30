import tensorflow as tf
import json
from tensorflow.keras.models import load_model
import numpy as np
import nltk
import random
import pickle

data = pickle.load(open("training_data", "rb"))
words = data['words']
tags = data['tags']
train_x = data['train_x']
train_y = data['train_y']

# nltk.download('punkt')
# nltk.download('wordnet')

with open('intents.json') as data:
    intents = json.load(data)

stemmer = nltk.wordnet.WordNetLemmatizer()

model = load_model('model.h5')


def sentence_cleanup(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [stemmer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence, words, show_details=False):
    sentence_words = sentence_cleanup(sentence)
    bag = [0]*len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w==s:
                bag[i]=1
                if show_details:
                    print('Found in bag: %s' %w)
    return (np.array(bag))

def classify(sentence):
    bag = bag_of_words(sentence, words)
    results = model.predict(bag.reshape(-1, len(words)))
    return np.argmax(results)

def response(sentence, userID='123', show_details=False):
    predicted_class=classify(sentence)
    predicted_tag = tags[predicted_class]
    for i in intents['intents']:
      if i['tag']==predicted_tag:
        return print(random.choice(i['responses']))

if __name__ == '__main__':
    response("I want to buy speakers")
