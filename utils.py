import re

def clean_comment(comment):
    # Changing to lowercase
    comment = comment.lower()
    
    # Changing he'll to he will
    comment = re.sub(r"i'm", "i am", comment)
    
    comment = re.sub(r"aren't", "are not", comment)
    comment = re.sub(r"couldn't", "counld not", comment)
    comment = re.sub(r"didn't", "did not", comment)
    comment = re.sub(r"doesn't", "does not", comment)
    comment = re.sub(r"don't", "do not", comment)
    comment = re.sub(r"hadn't", "had not", comment)
    comment = re.sub(r"hasn't", "has not", comment)
    comment = re.sub(r"haven't", "have not", comment)
    comment = re.sub(r"isn't", "is not", comment)
    comment = re.sub(r"it't", "had not", comment)
    comment = re.sub(r"hadn't", "had not", comment)
    comment = re.sub(r"won't", "will not", comment)
    comment = re.sub(r"can't", "cannot", comment)
    comment = re.sub(r"mightn't", "might not", comment)
    comment = re.sub(r"mustn't", "must not", comment)
    comment = re.sub(r"needn't", "need not", comment)
    comment = re.sub(r"shouldn't", "should not", comment)
    comment = re.sub(r"wasn't", "was not", comment)
    comment = re.sub(r"weren't", "were not", comment)
    comment = re.sub(r"won't", "will not", comment)
    comment = re.sub(r"wouldn't", "would not", comment)
    
    comment = re.sub(r"\'s", " is", comment)
    
    comment = re.sub(r"\'ll", " will", comment)
    
    comment = re.sub(r"\'ve", " have", comment)
    
    comment = re.sub(r"\'re", " are", comment)
    
    comment = re.sub(r"\'d", " would", comment)
    
    comment = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', comment, flags=re.MULTILINE)
    
    comment = re.sub(r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', '', comment)
    
    return comment

def check_comment_quality(comment):
    comment = comment.lower()
    if comment =='[deleted]' or comment == '[removed]':
        return False
    elif len(comment.split()) >= 2 and len(comment.split()) < 100:
        return True
    return False
    