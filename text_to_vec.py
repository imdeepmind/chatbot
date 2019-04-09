import pandas as pd
import pickle
import numpy as np

data = pd.read_csv('data/dataset.csv')

# Just for testing
data = data.head(1000)

questions = data['question'].values
answers = data['answer'].values

with open('data/tokenizer.pickle', 'rb') as t:
    tokenizer = pickle.load(t)
    
questions_vec = []
answers_vec = []

for question in questions:
    qvec = tokenizer.texts_to_sequences(question)
    questions_vec.append(qvec)
    
for answer in answers:
    avec = tokenizer.texts_to_sequences(answer)
    answers_vec.append(avec)
    
np.save('data/questons.npy', questions_vec)
np.save('data/answers.npy', answers_vec)