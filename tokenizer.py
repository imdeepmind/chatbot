import pandas as pd
from keras.preprocessing.text import Tokenizer
import pickle

VOCAB_SIZE = 10000

data = pd.read_csv('data/dataset.csv')

# Just for testing
data = data.head(1000)

questions = data['question'].values
answers = data['answer'].values

del data

t = Tokenizer(num_words=VOCAB_SIZE)

t.fit_on_texts(questions)
t.fit_on_texts(answers)

with open('data/tokenizer.pickle', 'wb') as tokenizer:
    pickle.dump(t, tokenizer)