from sklearn.feature_extraction.text import CountVectorizer
import importlib

importlib.import_module("janitor.py")

cv = CountVectorizer(stop_words='english')
data_cv = cv.fit_transform(cleandata.Transcripts)
data_dtm = pd.DataFrame(data_cv.toarray(), columns = cv.get_feature_names())
data_dtm.index = cleandata.index
print(data_dtm)
