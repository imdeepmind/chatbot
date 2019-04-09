import pandas as pd
import pickle
import numpy as np
from keras.preprocessing.sequence import pad_sequences

data = pd.read_csv('data/dataset.csv')

# Just for testing
data = data.head(1000)

questions = data['question'].values
answers = data['answer'].values

with open('data/tokenizer.pickle', 'rb') as t:
    tokenizer = pickle.load(t)
    
questions = tokenizer.texts_to_sequences(questions)
answers = tokenizer.texts_to_sequences(answers)

questions = pad_sequences(questions, maxlen=100, padding='post')
answers = pad_sequences(answers, maxlen=100, padding='post')

np.save('data/questions.npy', questions)
np.save('data/answers.npy', answers)