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

#1

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


df = pd.read_csv("C:/Users/sykri/OneDrive/CSCI E-101/Week 15/Section 15/ImmuneTea.csv")


tea = np.array(df.loc[(df['Drink'] == 'Tea'), "InterferonGamma"])
cof = np.array(df.loc[(df['Drink'] == 'Coffee'), "InterferonGamma"])

print(tea.shape,cof.shape)

equal_variance = EqualVar(tea, cof)
tTest = ttest_ind(tea,cof,equal_var = equal_variance)
results = tTest.statistic
Temp_P_Value = tTest.pvalue

print(results,Temp_P_Value)

# be aware of wording: higher or different
# Focus more on tw-tailed test


# 2

array1d = np.arange(1,11)
print("1-D array (vector) with 10 elements ->", array1d)

#you can change a vector to row or column  matrix

array_row_matrix =  array1d.reshape(-1,1)
print("\nvector converted to a row matrix  ->\n", array_row_matrix)

array_col_matrix =  array1d.reshape(1,-1)
print("\nvector converted to a column matrix  ->\n", array_col_matrix)


array_2d =  array1d.reshape(5,2)
print("\nvector converted to a 5 X 2 2-D array->\n", array_2d)

# solution
array1d = np.arange(0,30)
print(array1d)
array_2d =  array1d.reshape(5,6)
print("\nvector converted to a 5 X 6 2-D array->\n", array_2d)


# 3
#sales is dep
df = pd.read_csv("C:/Users/sykri/OneDrive/CSCI E-101/Week 15/Section 15/advertising.csv")
print(df.head(2))
#run the cell below
regression_model = sm.ols(formula="Sales~TV+Radio+Newspaper",data=df)
results = regression_model.fit()
print(results.summary())

#your code here to extract the significant predictors, and store it in a dataframe.
# # Calls for data for ols
# print (Results.summary())

# Results.params
# Results.f_pvalue
# Results.pvalues
# Results.pvalues.x
# Results.pvalues.y
sig = df.drop(["Newspaper", "Sales"], axis=1)
# How do i iterate thru t-test values and select significant variables??? see code
sig_dict = {}
for key, value in results.pvalues.to_dict().items():
    if key != "Intercept":
        if value <= 0.05:
            sig_dict[key] = value

print(sig_dict)
print(results.pvalues)

#your code to print the r-square and adj r-square values.
print(results.rsquared_adj)
print(results.rsquared)

#show the df
print(sig)
# TV & radio
# look at solution


# 4

X= df.drop("Sales", axis=1)
y= df['Sales']

x_train,x_test,y_train,y_test = train_test_split(X, y, test_size=0.3, random_state=1)
model = LinearRegression()
model.fit(x_train,y_train)

print(model.score(x_train, y_train))
print(model.score(x_test, y_test))
print(model.coef_)
print(model.intercept_)

# equation: y = 0.0470x1 + 0.177x2 + 0.002x3 + 2.937
# how to determine which variable is which coef?

# predict
# print(x_test.tail())
# x = x_test.append([[200,100,100]])
# print(x.tail())
predicted = model.predict([[200, 100, 100]])
print(predicted)

predicted = model.predict([[200, 100, 0]])
print(predicted)
# sales would slightly decrease
# slope is small


# 5
df = pd.read_csv("C:/Users/sykri/OneDrive/CSCI E-101/Week 15/Section 15/default.csv")
print(df.head())
y = df["default"].map({'Yes':1, 'No':0})
student = pd.get_dummies(df.student, prefix='student', drop_first=True)
print(student.head())
df.drop(["student","default"],axis =1,inplace=True)
x = pd.concat([df,student], axis="columns")
print(x.head())

# From solution
# df['default'] = (df['default'] == "Yes")*1
# df = pd.get_dummies(df, columns=['student'], prefix='student', drop_first=True)

# logistic regression penalty='none'. USE WHATS TAUGHT IN CLASS
x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.3, random_state=1)

log_model = LogisticRegression(penalty="none")
log_model.fit(x_train, y_train)

y_pred_test = log_model.predict(x_test)

score_train = log_model.score(x_train,y_train)
score_test = log_model.score(x_test,y_test)

from sklearn.metrics import confusion_matrix
cf_matrix = confusion_matrix(y_test, y_pred_test)
print(cf_matrix)

print(f'The accuracy for train set is {score_train:4f}')
print(f'The accuracy for test set is {score_test:4f}')


#6
class BankAccount:
    def __init__(self, name, account_number,address):
        self.__name = name
        self.__account_number = account_number
        self.address = address

class CreditCard(BankAccount):
    def __init__(self, name, account_number, address,
                    credit_card_number, credit_line):
        super().__init__(name, account_number,address)
        self.__credit_card_number = credit_card_number
        self.__credit_line = credit_line
        self.__balance = 0
        self.__credit_available = credit_line
        self.__transact_dict = {}
        self.__transaction_id = 1000001

    def get_balance(self):
        return self.__balance

    def Transact(self, description, amount):
        """
        Simulates a transaction of a credit card with the following rules :

        1. transcation should only go through if the credit available is greater than or equal
        to the amount of transaction.

        2. If the transaction is success , assign a unique transaction id , and store each of the transaction in
        a dictionary with transaction id as key, and description, amount, and current balance as value in a list.
        The dictionary should be declared in the constructor.
        Example to store your transactions in dict called transact_dict:
        self.__transact_dict [transaction_id] = [description, amount, balance]

        3. Keeps track of credit available and balance at each transaction

        :param description: string, the description of the transaction
        :param amount: float, the transaction amount

        :returns : the string success if the transaction goes through , declined otherwise

        """
        if self.__credit_available >= amount:
            self.__balance += amount
            self.__credit_available = self.__credit_line - amount
            self.__transact_dict[self.__transaction_id] = [description,amount,self.__balance]
            self.__transaction_id += 1
            return("success")
        else:
            return("declined")

        # your code here

    def Statement(self):
        stat = pd.DataFrame(self.__transact_dict.keys(), columns=['TransactionId'])
        temp = np.array(list(self.__transact_dict.values()))
        stat['Description'] = temp[:, 0]
        stat['amount'] = temp[:, 1]
        stat['balance'] = temp[:, 2]
        stat.set_index(stat['TransactionId'], inplace=True)
        stat.drop('TransactionId', axis=1, inplace=True)
        print(stat)



# create an account for Toph -> name , account number, address, credit card number, credit limit
toph = CreditCard("Toph Beifong", "10004001", "Dallas", "1000100001333333", 100000)
print(toph.Transact("EVDealership TSLA", 70000))
print(toph.get_balance())
print(toph.Transact("EVDealership TSLA SUV", 100000))
print(toph.Transact("Target ", 100))
toph.Statement()

# create an account for Aang -> name , account number, address, credit card number, credit limit
aang = CreditCard("Aang Avatar", "10004001", "Austin", "1000100001333334", 10000)
print(aang.Transact("EVDealership TSLA", 35000))
print(aang.get_balance())
print(aang.Transact("North Face", 100))
aang.Statement()



# # 7
# NLP
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

ex_str ="I bought this for my husband who plays the piano.  He is having a wonderful time playing these old hymns.\
The music  is at times hard to read because we think the book was published for singing from more than playing from.\
Great purchase though!"

#We will split the sentence into words
my_words = word_tokenize(ex_str.strip())
my_words

print("Stopwords in English:\n\n", stopwords.words("english"))

#filter our text by removing stopwords
MyStopWords = set(stopwords.words("english"))
filteredWords = []
for word in my_words:
    if word not in MyStopWords and word.isalpha():
        filteredWords.append(word)
print(filteredWords)


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