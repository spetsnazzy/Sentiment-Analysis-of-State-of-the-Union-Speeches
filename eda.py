import pickle
import pandas as pd

data = pd.read_pickle('data_term_matrix.pickle')
data = data.transpose()
# print(data.head())

top_dict = {}
for each in data.columns:
    top = data[each].sort_values(ascending=False).head(30)
    top_dict[each] = list(zip(top.index, top.values))

for presidents, top_words in top_dict.items():
    print(presidents)
    print(', '.join([word for word, count in top_words[0:14]]))
    print('-----')
