import sqlite3
import pandas as pd

def find_parent(parent_id):
    sql = """ SELECT * FROM comments WHERE parent_id = "{}" """.format(parent_id)
    c.execute(sql)
    result = c.fetchall()
    
    if result == None:
        return False
    return result
    

connection = sqlite3.connect('data/dataset.db')
c = connection.cursor()

conversation_pairs = []

sql = """ SELECT count(*) FROM comments"""
c.execute(sql)
total, = c.fetchone()

for i in range(1, total+1):
    sql = """ SELECT * FROM comments LIMIT {}, 1""".format(i)
    c.execute(sql)
    comment_id, parent_id, comment, subreddit = c.fetchone()
    
    parent = find_parent(comment_id)

    if parent:
        for p in parent:
            _, _, reply, _ = p
            conversation_pairs.append([comment, reply])

dataframe = pd.DataFrame(conversation_pairs, columns=['msg', 'reply'])
dataframe.to_csv('conversation.csv', index=False)