import sqlite3
import pandas as pd

connection = sqlite3.connect('data/dataset.db')
c = connection.cursor()

df = pd.read_sql_query('SELECT parent, comment FROM parent_reply WHERE parent NOT NULL AND score > 0', connection)

df.columns = ['question', 'answer']

df.to_csv('data/dataset.csv', index=False)