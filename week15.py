import nltk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# pip install tingo
from tiingo import TiingoClient

# # Tiingo API
#
# # Tiingo API
# # prepare api key
# config = {}
#
# # create config dictionary to store api key
# config['api_key'] = '543de6ade1a68bb9ff63f855e6e8985a43f58dfa' # tiingo acct sykrishukor
#
# # include a session key to enable reuse of the same HTTP Session for all api calls
# config['session'] = True
#
# # ionitialize TiingoClient object instance w. session and api keys
# client = TiingoClient(config)
#
# Results = client.get_ticker_price("AAPL", fmt='json',
#                                       startDate='2021-01-01',
#                                       endDate='2021-12-08',
#                                       frequency='daily')
# print(Results)
#
# # Converting list to
# df = pd.DataFrame(Results)
#
# # Filtering dataset
# df_filter = (df['close'] <= (df['open']))
# method1 = df[df_filter]
#
# method2 = df[(df['close']==df['close'].min())]
#
# print(method1)
# print(method2)
#
# # List tickers. returns as tuple dictionary {'x1':'y1'},{'x2':'y2'}
# tickers = client.list_stock_tickers()
# print(tickers)
#
# # Convert list to df
# tkr = pd.DataFrame(tickers)
# print(tkr.tail(20))




# # pandas_datareader
#
# import seaborn as sns
# import pandas_datareader.data as rdr
# import datetime as dt
#
# # Assign start dates
# start = dt.datetime(2020,3,1)
# end = dt.datetime(2021,12,1)
#
# # use pandas_datareader.data to grab stock from stooq
# df = rdr.DataReader("tsm","stooq",start,end)
# print(df[["Close"]].max())
# plt.plot(df[["Open","Close"]])
# (sns.pairplot(df))
# plt.show()


# # Take tables from wwebsite
#
# IRSTable = pd.read_html('https://www.irs.gov/publications/p15t#en_US_2019_publink100020274')
# print(IRSTable)
#
# type(IRSTable)
# df = pd.DataFrame(IRSTable[0])
# print(df)
#
# df.rename(columns= {0: 'Payroll_Period', 1:'Add_Additional'}, inplace = True)
# print(df)
#
# df = df.drop(labels=range(0, 2), axis=0)


# # Reading text from .pdf
#
# import PyPDF2 as pdf
#
# # Opening pdf page
# myFile = open("starwars.pdf","rb")
# PDFrdr = pdf.PdfFileReader(myFile)
#
# PageText = PDFrdr.getPage(0)
# print(PageText.extractText())
#
# myFile.close()
#
# # Opening multiple .pdf pages
# with open('starwarspages.pdf', 'rb') as myFile:
#     PDFrdr = pdf.PdfFileReader(myFile)
#     for page_num in range(PDFrdr.numPages):
#         PageText = PDFrdr.getPage(page_num)
#         print(PageText.extractText())
#
# myFile.close()


# # NLP
#
# # Read text file and readlines
# myfile = open("cto.txt", "r")
# lines = myfile.readlines()
# myfile.close()
#
# mystr = ""
# for line in lines:
#     line = line.strip()
#     mystr = mystr + line
#
# print(mystr)
#
# import nltk
# # nltk.download("all")
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk import FreqDist
# from nltk.stem import PorterStemmer
# from nltk.stem import WordNetLemmatizer
#
# my_words = word_tokenize(mystr.lower())
# print(my_words, "\n")
#
#   # Stop Words: A stop word is a commonly used word (such as “the”, “a”, “an”, “in”)
# mystopwords = set(stopwords.words("english"))
#
# print(mystopwords)
#
# filtered_words = []
# for word in my_words:
#     if word not in mystopwords and word.isalpha():
#         filtered_words.append(word)
#
# print(filtered_words)
#
# ps = PorterStemmer()
#
# # stemming words
# stemmed_words = []
# for word in filtered_words:
#     stemmed_words.append(ps.stem(word))
# print("stemmed words: ", stemmed_words)
#
# freq = FreqDist(stemmed_words)
#
# for word, frequency in freq.most_common(10):
#     print("{}:{}".format(word, frequency))
#
#
# freq.plot(30, title =  "Top 30 from review", linewidth = 10, color = "g")



# NLP Lemmatizer

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

lemmatizer = WordNetLemmatizer()
# word = "skies"
# print(lemmatizer.lemmatize(word))
#
# word = "writing"
# print(lemmatizer.lemmatize(word, pos="v"))
#
# word = "better"
# print(lemmatizer.lemmatize(word, pos="a"))
#
# word = "feet"
# print(lemmatizer.lemmatize(word))
#
# word = "exhausted"
# print(lemmatizer.lemmatize(word, pos="v"))

# convert str into tokens (without pos tags)
string = "my ass is so tight I'm shitting diamonds and breaking my toilet bowl, haha, just joking, only in GTA though"
# list = nltk.word_tokenize(string)
#
# lemmatized_string = ' '.join([lemmatizer.lemmatize(words) for words in list])
# print(lemmatized_string)

# convert str into tokens w/ appropritate pos tags
# Define function to lemmatize each word with its POS tag

# POS_TAGGER_FUNCTION : TYPE 1
def pos_tagger(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

pos_tagged = nltk.pos_tag(nltk.word_tokenize(string))
print(pos_tagged)
# As you may have noticed, the above pos tags are a little confusing.

# we use our own pos_tagger function to make things simpler to understand.
wordnet_tagged = list(map(lambda x: (x[0], pos_tagger(x[1])), pos_tagged))
print(wordnet_tagged)

lemmatized_sentence = []
for word, tag in wordnet_tagged:
    if tag is None:
        # if there is no available tag, append the token as is
        lemmatized_sentence.append(word)
    else:
        # else use the tag to lemmatize the token
        lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
lemmatized_sentence = " ".join(lemmatized_sentence)

print(lemmatized_sentence)