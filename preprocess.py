import json
import re

def check_comment_quality(comment):
    comment = comment.lower()
    if comment =='[deleted]' or comment == '[removed]':
        return False
    elif len(comment.split()) >= 2 and len(comment.split()) < 100:
        return True
    return False
    
def clean_comment(comment):
    comment = comment.lower()
    
    comment = re.sub(r"i'm", "i am", comment)
    comment = re.sub(r"he's", "he is", comment)
    comment = re.sub(r"she's", "she is", comment)
    comment = re.sub(r"that's", "that is", comment)
    comment = re.sub(r"what's", "what is", comment)
    comment = re.sub(r"where's", "where is", comment)
    comment = re.sub(r"\'ll", "will", comment)
    comment = re.sub(r"\'ve", "have", comment)
    comment = re.sub(r"\'re", "are", comment)
    comment = re.sub(r"\'d", "would", comment)
    comment = re.sub(r"won't", "will not", comment)
    comment = re.sub(r"can't", "cannot", comment)
    
    comment = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', comment, flags=re.MULTILINE)
    
    comment = re.sub(r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', '', comment)
    
    comment = re.sub(r'"', '', comment)
    comment = re.sub(r'\'', '', comment)
    
    comment = re.sub(r'\n', '', comment)
    comment = re.sub(r'\d', '', comment)
    comment = re.sub(r'\t', '', comment)
    
    return comment
    
    
def main():
    with open('data/RC_2015-01', buffering=1000) as dataset:
        counter = 0
        for row in dataset:
            counter += 1
            
            data = json.loads(row)
            
            if data['score'] > 3:
                if check_comment_quality(data['body']):
                    comment = clean_comment(data['body'])
                    subreddit = data['subreddit']
                    parent_id = data['parent_id']
                    comment_id = data['name']
                    
                    print(comment, subreddit, parent_id, comment_id)

            if counter % 1000 == 0:
                print('--Currently preprocessing comment {}--'.format(counter))
    
if __name__ == '__main__':
    main()