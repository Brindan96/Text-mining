# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:36:54 2020

@author: Hp
"""
# Reviews from amazon.in for MI LED TV


import requests
from bs4 import BeautifulSoup as bs
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re

# Creating empty list 
MI_tv = []

# Extracting reviews 

for i in range(1,200):
  ip=[]  
  #url=https://www.amazon.in/Mi-Inches-Full-Android-Black/product-reviews/B07T89Z35Z/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1
  url = "https://www.amazon.in/Mi-Inches-Full-Android-Black/product-reviews/B07T89Z35Z/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber="+str(i)
  response = requests.get(url)
  soup = bs(response.content,"html.parser")# creating soup object to iterate over the extracted content 
  reviews = soup.findAll("span",attrs={"class","a-size-base review-text review-text-content"})
  # Extracting the content under specific tags  
  
  for i in range(len(reviews)):
    ip.append(reviews[i].text)  
  MI_tv=MI_tv+ip

MI_tv_rev = " ".join(MI_tv)

#removing symbols and making everyline into small case and removing numbers from extracted reviews 
MI_tv_rev = re.sub("[^A-Za-z" "]+"," ",MI_tv_rev).lower()
MI_tv_rev = re.sub("[0-9" "]+"," ",MI_tv_rev)

# spliting words 
MI_tv_rev_words = MI_tv_rev.split(" ")


# importing stopwords and removing it from extracted reviews 
with open("E:\\Data Science\\Data Science\\Assignemnts\\Brindan\\text mining\\stop.txt","r") as sw:
    stop = sw.read()

stopwords = stop.split("\n")

MI_tv_rev_words = [w for w in MI_tv_rev_words if not w in stopwords]

# joining the reviews
MI_tv_rev = " ".join(MI_tv_rev_words)


# Worldcloud
wordcloud_MI_tv = WordCloud(
                      background_color='black',
                      width=2000,
                      height=1800
                     ).generate(MI_tv_rev)

plt.imshow(wordcloud_MI_tv)


# Positive words

with open("E:\\Data Science\\Data Science\\Assignemnts\\Brindan\\text mining\\positive-words.txt","r") as pos:
  poswords = pos.read().split("\n")
  
poswords = poswords[36:]

# Positive Worldcloud
MI_tv_positive = " ".join ([w for w in MI_tv_rev_words if w in poswords])
wordcloud_MI_tv_positive = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(MI_tv_positive)

plt.imshow(wordcloud_MI_tv_positive)


# Negative Worldcloud
with open("E:\\Data Science\\Data Science\\Assignemnts\\Brindan\\text mining\\negative-words.txt","r") as neg:
  negwords = neg.read().split("\n")

MI_tv_negative = " ".join ([w for w in MI_tv_rev_words if w in negwords])

wordcloud_MI_tv_negative = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(MI_tv_negative)

plt.imshow(wordcloud_MI_tv_negative)











# Extracting reviews from snapdeal

iphone = []

# Extracting reviews 

for i in range(1,70):
  ip=[]  
  
  url = "https://www.snapdeal.com/product/apple-iphone-6s-32gb-space/647328495952/reviews?page="+str(i)
  url1 = "&sortBy=HELPFUL#defRevPDP"
  response = requests.get(url,url1)
  soup = bs(response.content,"html.parser")# creating soup object to iterate over the extracted content 
  reviews = soup.findAll("span",attrs={"class","a-size-base review-text review-text-content"})
  # Extracting the content under specific tags  
  
  for i in range(len(reviews)):
    ip.append(reviews[i].text)  
  iphone=iphone+ip

iphone_rev = " ".join(MI_tv)

#removing symbols and making everyline into small case and removing numbers from extracted reviews 
iphone_rev = re.sub("[^A-Za-z" "]+"," ",iphone_rev).lower()
iphone_rev = re.sub("[0-9" "]+"," ",iphone_rev)

# spliting words 
iphone_rev_words = iphone_rev.split(" ")


# importing stopwords and removing it from extracted reviews 
with open("F:\\Data Science\\Assignemnts\\Brindan\\text mining\\stop.txt","r") as sw:
    stop = sw.read()

stopwords = stop.split("\n")

iphone_rev_words = [w for w in iphone_rev_words if not w in stopwords]

# joining the reviews
iphone_rev = " ".join(iphone_rev_words)


# Worldcloud
wordcloud_iphone = WordCloud(
                      background_color='black',
                      width=2000,
                      height=1800
                     ).generate(iphone_rev)

plt.imshow(wordcloud_iphone)


# Positive words

with open("F:\\Data Science\\Assignemnts\\Brindan\\text mining\\positive-words.txt","r") as pos:
  poswords = pos.read().split("\n")
  
poswords = poswords[36:]

# Positive Worldcloud
iphone_positive = " ".join ([w for w in iphone_rev_words if w in poswords])
wordcloud_iphone_positive = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(iphone_positive)

plt.imshow(wordcloud_iphone_positive)


# Negative Worldcloud
with open("F:\\Data Science\\Assignemnts\\Brindan\\text mining\\negative-words.txt","r") as neg:
  negwords = neg.read().split("\n")

iphone_negative = " ".join ([w for w in iphone_rev_words if w in negwords])

wordcloud_iphone_negative = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(iphone_negative)

plt.imshow(wordcloud_iphone_negative)










# IMDB reviews

# Creating empty list 
Joker = []

# Extracting reviews 

for i in range(1,200):
  ip=[]  
  
  url = "https://www.imdb.com/title/tt7286456/reviews?sort=submissionDate&dir=desc&ratingFilter=0"+str(i)
  response = requests.get(url)
  soup = bs(response.content,"html.parser")# creating soup object to iterate over the extracted content 
  reviews = soup.findAll("span",attrs={"class","a-size-base review-text review-text-content"})
  # Extracting the content under specific tags  
  
  for i in range(len(reviews)):
    ip.append(reviews[i].text)  
  Joker=Joker+ip

Joker_rev = " ".join(Joker)

#removing symbols and making everyline into small case and removing numbers from extracted reviews 
Joker_rev = re.sub("[^A-Za-z" "]+"," ",Joker_rev).lower()
Joker_rev = re.sub("[0-9" "]+"," ",Joker_rev)

# spliting words 
Joker_rev_words = Joker_rev.split(" ")


# importing stopwords and removing it from extracted reviews 
with open("F:\\Data Science\\Assignemnts\\Brindan\\text mining\\stop.txt","r") as sw:
    stop = sw.read()

stopwords = stop.split("\n")

Joker_rev_words = [w for w in Joker_rev_words if not w in stopwords]

# joining the reviews
Joker_rev = " ".join(Joker_rev_words)


# Worldcloud
wordcloud_Joker = WordCloud(
                      background_color='black',
                      width=2000,
                      height=1800
                     ).generate(Joker_rev)

plt.imshow(wordcloud_Joker)


# Positive words

with open("F:\\Data Science\\Assignemnts\\Brindan\\text mining\\positive-words.txt","r") as pos:
  poswords = pos.read().split("\n")
  
poswords = poswords[36:]

# Positive Worldcloud
Joker_positive = " ".join ([w for w in Joker_rev_words if w in poswords])
wordcloud_Joker_positive = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(Joker_positive)

plt.imshow(wordcloud_Joker_positive)


# Negative Worldcloud
with open("F:\\Data Science\\Assignemnts\\Brindan\\text mining\\negative-words.txt","r") as neg:
  negwords = neg.read().split("\n")

Joker_negative = " ".join ([w for w in Joker_rev_words if w in negwords])

wordcloud_Joker_negative = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(Joker_negative)

plt.imshow(wordcloud_Joker_negative)



