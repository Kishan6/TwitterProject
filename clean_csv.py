# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 14:28:44 2021

@author: Kishan Pani
"""

import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
import io
df2 = pd.read_csv('control_tweets.csv')
# Dataset is now stored in a Pandas Dataframe

df2.head()

df3 = df2.loc[:, ["tweet","class"]]

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,6))
df3.groupby('class').tweet.count().plot.bar(ylim=0)
plt.show()

"""#Clean Data"""

# from https://towardsdatascience.com/cleaning-text-data-with-python-b69b47b97b76
import re

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
import string
from nltk.corpus import stopwords
# # In case of any corpus are missing 
# download all-nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger') 
stop_words = stopwords.words("english")
from nltk.stem import WordNetLemmatizer
wordnet = WordNetLemmatizer()
def text_preproc(x):
  x = x.lower()
  x = ' '.join([word for word in x.split(' ') if word not in stop_words])
  x = x.encode('ascii', 'ignore').decode()
  x = re.sub(r'https*\S+', ' ', x)
  x = re.sub(r'@\S+', ' ', x)
  x = re.sub(r'#\S+', ' ', x)
  x = re.sub(r'\'\w+', '', x)
  x = re.sub('[%s]' % re.escape(string.punctuation), ' ', x)
  x = re.sub(r'\w*\d+\w*', '', x)
  x = re.sub(r'\s{2,}', ' ', x)
  return x

def numberize(x):
  if (x == 'depressed'):
    return (0)
  else:
    return (1)

# clean data
print(df3.to_numpy()[5][0])
print(text_preproc(df3.to_numpy()[5][0]))
df3["tweet"] = df3["tweet"].apply(lambda x: text_preproc(x))
df3["class"] = df3["class"].apply(lambda x: numberize(x))

df3.to_csv('control_clean.csv')