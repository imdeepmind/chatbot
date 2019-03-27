import json
from utils import clean_comment, check_comment_quality

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
                    print('')

            if counter % 1000 == 0:
                print('--Currently preprocessing comment {}--'.format(counter))
    
if __name__ == '__main__':
    main()