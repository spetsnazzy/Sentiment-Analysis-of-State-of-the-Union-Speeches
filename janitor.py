import pickle
import pandas as pd
import re
import string

presidents = ['obama', 'bush', 'clinton', 'reagan', 'nixon']

data = {}

# Assigns transcripts to corresponding president
for i, c in enumerate(presidents):
    with open("transcripts/" + c + ".pickle", "rb") as file:
        data[c] = pickle.load(file)

def combine_text(listoftext):
    combinedtext = ''.join(listoftext)
    return combinedtext

# Makes all letters lowercase, removes punctuation
def clean_textr1(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

# Combines transcripts and president keys
datacombined = {key: [combine_text(value)] for (key, value) in data.items()}

pd.set_option('max_colwidth', 150)

# Creates the table
data_df = pd.DataFrame.from_dict(datacombined).transpose()
data_df.columns = ['transcript']
data_df = data_df.sort_index()

# Lambda def of first round cleaning function
round1 = lambda x: clean_textr1(x)
cleandata = pd.DataFrame(data_df.transcript.apply(round1))
