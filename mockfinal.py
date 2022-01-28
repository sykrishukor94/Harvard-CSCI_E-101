import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import scipy.stats as stat
from scipy.stats import ttest_rel
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

#4
islands = [10,6,8,1,3,9,1,10,10,4,5,9]
foods = [8,7,8,8,6,10,8,9,9,6,5,8]

def EqualVar(arr1, arr2):
    EqualVar = True
    print(arr1.std(),arr2.std())
    if arr1.std() > arr2.std():
        if arr1.std() / arr2.std() > 2:
            EqualVar = False
    else:
        if arr2.std() / arr1.std() > 2:
            EqualVar = False

    return EqualVar

df = pd.DataFrame(data=[islands,foods])

print(df)

equal_variance = EqualVar(islands, foods)
tTest = ttest_ind(islands,foods,equal_var = equal_variance)
results = tTest.statistic
Temp_P_Value = tTest.pvalue



# 7
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

str = pd.read_csv("interview.txt")

my_words = word_tokenize(str.strip())

#filter our text by removing stopwords
MyStopWords = set(stopwords.words("english"))
filteredWords = []
for word in my_words:
    if word not in MyStopWords and word.isalpha():
        filteredWords.append(word)

#reduce the words in to their simpler forms
ps = PorterStemmer()
stemWords = []

for word in filteredWords:
    stemWords.append(ps.stem(word))

print(stemWords)

#You can look at the frequency, and plot it to see which words appear more frequently.
freq = FreqDist(stemWords)

for word, frequency in freq.most_common(10):
      print("{}:{}".format(word, frequency))

#plot frequency for top 30
freq.plot(10,title="Top 10 words", linewidth=10, color="g")
plt.show()

