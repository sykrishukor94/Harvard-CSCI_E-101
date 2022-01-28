# import Packages
import nltk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns


# VIF for Multicollinearity Testing
from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd

# For oneway ANOVA
import scipy.stats as st

# For Post Hoc
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison as multi

# For adding constant fot vif
from statsmodels.tools.tools import add_constant

# # 8
# class employees:
#     def __init__(self, employee_ID, LastName, FirstName, dept_no, salary, active):
#         self.employee_ID = employee_ID # int
#         self.FirstName = FirstName # str
#         self.LastName = LastName # str
#         self.dept_no = dept_no
#         self.__salary = salary
#         self.active = active
#
#     def getSalary(self):
#         return self.__salary
#
#     def setSalary(self, salary):
#         self.__salary = salary

# 14
# import packages
# Islnds > foods
# import pandas as pd
# from scipy.stats import ttest_ind
#
# # load raw datrra
# islands = [10,6,8,1,3,9,1,10,10,4,5,9]
# foods = [8,7,8,8,6,10,8,9,9,6,5,8]
#
# # function to test for equal variance
# def EqualVar(arr1, arr2):
#     EqualVar = True
#     # print(arr1.std(),arr2.std())
#     if arr1.std() > arr2.std():
#         if arr1.std() / arr2.std() > 2:
#             EqualVar = False
#     else:
#         if arr2.std() / arr1.std() > 2:
#             EqualVar = False
#     # print(EqualVar)
#     return EqualVar
#
# # Setup np array and df
# islands = np.array(islands)
# foods = np.array(foods)
# df = pd.DataFrame(data=[islands,foods])
#
# # print(df)
#
# # run equal variance and input results into independent two-tailed ttest
# equal_variance = EqualVar(islands, foods)
# tTest = ttest_ind(islands,foods,equal_var = equal_variance, alternative="greater")
#
# # store results and p-value
# results = tTest.statistic
# Temp_P_Value = tTest.pvalue
#
# print(results)
# print(Temp_P_Value)


# 15

dayofweek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Mon"]
revenue = ["1000.87", "2344.67", "2050.56", "1890.53", "677.54", "1120.91"]
tables = [25,43,38,30,16,30]

df = pd.DataFrame(dayofweek)
df["revenue"] = revenue
df["tables"] = tables
print(df)

df['breakeven'] = df.apply(lambda row: "yes" if row.tables >=30 else "no", axis=1)
print(df)

