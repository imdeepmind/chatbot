import json
import sqlite3
from utils import clean_comment, check_comment_quality

connection = sqlite3.connect('data/dataset.db')
c = connection.cursor()

transaction_array = []

def create_table():
    sql = """CREATE TABLE IF NOT EXISTS comments (
        comment_id TEXT PRIMARY KEY NOT NULL,
        parent_id TEXT,
        comment TEXT,
        subreddit TEXT
    )"""
    
    c.execute(sql)
    
def transaction_builder(sql):
    global transaction_array
    if len(transaction_array) > 1000:
        c.execute('BEGIN TRANSACTION')
        for s in transaction_array:
            try:
                c.execute(s)
            except:
                return False
        connection.commit()
        transaction_array = []
        print('--Saving the data into the database--')
    else:
        transaction_array.append(sql)
    
    return True
    
    
def add_data(comment_id, parent_id, comment, subreddit):
    sql = """ INSERT INTO comments (comment_id, parent_id, comment, subreddit ) 
    VALUES ("{}", "{}", "{}", "{}")""".format(comment_id, parent_id, comment, subreddit)
    
    transaction_builder(sql)

def main():
    create_table()
    with open('data/RC_2015-01', buffering=10000) as dataset:
        counter = 0
        for row in dataset:
            data = json.loads(row)
            if data['score'] > 3:
                if check_comment_quality(data['body']):
                    comment = clean_comment(data['body'])
                    subreddit = data['subreddit']
                    parent_id = data['parent_id']
                    comment_id = data['name']
                    
                    add_data(comment_id, parent_id, comment, subreddit)
                    
                    counter += 1
                    
                    if counter % 1000 == 0:
                        print('--Currently preprocessing comment {}--'.format(counter))
    
if __name__ == '__main__':
    main()