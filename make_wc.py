# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 14:08:23 2021

@author: Kishan Pani
"""

# Python program to generate WordCloud
  
# importing all necessery modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
  
# Reads 'Youtube04-Eminem.csv' file 
df = pd.read_csv(r"depressed_clean.csv")
  
comment_words = ''
stopwords = set(STOPWORDS)
  
# iterate through the csv file
for val in df.tweet:
      
    # typecaste each val to string
    val = str(val)
  
    # split the value
    tokens = val.split()
    tokens2 = []
      
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
        if (len(tokens[i]) != 1):
            tokens2.append(tokens[i])

    comment_words += " ".join(tokens2)+" "
  
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)
  
# plot the WordCloud image                       
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
  
plt.savefig('depressed_wordcloud.png', dpi=300)