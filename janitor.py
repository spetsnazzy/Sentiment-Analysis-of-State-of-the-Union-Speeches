import pickle
import pandas as pd
import re
import string
from sklearn.feature_extraction.text import CountVectorizer

presidents = ['Obama', 'Bush', 'Clinton', 'Reagan', 'Nixon']

data = {}

# Assigns transcripts to corresponding president
for i, c in enumerate(presidents):
    with open("transcripts/" + c + ".pickle", "rb") as file:
        data[c] = pickle.load(file)

def combine_text(listoftext):
    combinedtext = ''.join(listoftext)
    return combinedtext

# Makes all letters lowercase, removes punctuation
def cleaner(text):
    # Makes all text lowercase
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    # Removes digits
    text = re.sub('[0123456789]', '', text)
    text = re.sub('\w*\d\w*', '', text)
    # Removes new lines and \r
    text = re.sub('[\n\r]', '', text)
    # Removes instances of the word transcript
    text = re.sub('transcript', '', text)
    return text
    # Hyphens and apostrophes have not been removed


# Combines transcripts and president keys
datacombined = {key: [combine_text(value)] for (key, value) in data.items()}

pd.set_option('max_colwidth', 150)

# Creates the table
data_df = pd.DataFrame.from_dict(datacombined).transpose()
data_df.columns = ['Transcripts']
data_df = data_df.sort_index()

# Lambda def of first round cleaning function
round1 = lambda x: cleaner(x)
cleandata = pd.DataFrame(data_df.Transcripts.apply(round1))


data_df.to_pickle("corpus.pickle")

###########################################################

cv = CountVectorizer(stop_words='english')
data_cv = cv.fit_transform(cleandata.Transcripts)
data_dtm = pd.DataFrame(data_cv.toarray(), columns = cv.get_feature_names())
data_dtm.index = cleandata.index
print(data_dtm)
