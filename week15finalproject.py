# import packages
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

# # df cleanup functions from Module 7
# def CleanColumnHeading(dfx):
# # Your code to convert all column names to lower cases
#     dfx.rename(columns = str.lower, inplace=True)
# # Your code to change all spaces in column names to underscore
#     dfx.rename(columns = {col: col.replace(' ','_') for col in dfx.columns}, inplace = True)
# # standardizes state column header names AFTER undercase and underscore transformation
#     dfx.rename({'%state%': 'state'}, axis = 1, inplace = True)
#     return dfx
#
#
# # Load datasets by state. Focus on WA, CA and OR
# # Homelessness from .csv
# homeless_df = pd.read_csv("C:/Users/sykri/OneDrive/CSCI E-101/Final Project/USAHomelessPopulation2021.csv")
# # Household income from .csv
# income_df = pd.read_csv("C:/Users/sykri/OneDrive/CSCI E-101/Final Project/USAMedianIncome2021.csv")
# # Education Attainment .csv
# edu_df = pd.read_csv("C:/Users/sykri/OneDrive/CSCI E-101/Final Project/USAEducationAttainment.csv")
# # Unemployment Benefits by state .csv
# unempb_df = pd.read_csv("C:/Users/sykri/OneDrive/CSCI E-101/Final Project/USAUnemploymentBenefits2021.csv")
# # Unemploymeny Rate by state .csv
# unemprate_df = pd.read_csv("C:/Users/sykri/OneDrive/CSCI E-101/Final Project/USAUnemploymentRate2021.csv")
# # Cost of living index by state (OPTIONAL)
# cost_df = pd.read_csv("C:/Users/sykri/OneDrive/CSCI E-101/Final Project/USACostofLivingIndex2021.csv")
# # Population from .csv
# pop_df = pd.read_csv("C:/Users/sykri/OneDrive/CSCI E-101/Final Project/USAPopulation2021.csv")
# # Avg temperature from .csv; convert to
# temp_df = pd.read_csv("C:/Users/sykri/OneDrive/CSCI E-101/Final Project/USAAvgTemperature2021.csv")
# # Veterans per state
# vet_df = pd.read_csv("C:/Users/sykri/OneDrive/CSCI E-101/Final Project/USAVeterans2021.csv")
#
#
# datasets = [homeless_df,income_df,edu_df,unempb_df,unemprate_df,cost_df,temp_df,pop_df,vet_df]
#
# for x in datasets:
#     CleanColumnHeading(x)
#     print(x.info())
#
# df = pd.DataFrame(homeless_df)
# for x in datasets[1:]:
#     df = pd.merge(df,x,on='state')
#
# print(df.info())
#
# # Save data frame to CSV file
# df.to_csv("C:/Users/sykri/OneDrive/CSCI E-101/Final Project/finalHomelessFactors.csv", index= False)

#                                       End of Part 1


# Load finalHomelessFactors dataset
df = pd.read_csv("C:/Users/sykri/OneDrive/CSCI E-101/Final Project/finalHomelessFactorsXS.csv")

# Normalizing total homelessness/total*1,000,000 populaiton to get homeless people per capita
df["homelesscpt"] = df["totalhomeless"]/df["pop"]

# # Selecting 10 factors
# new_df = df[["homelesscpt","householdincome", "percenthighschoolorhigher","percentbachelorsorhigher" ,"unemploymentrate", "costindex", "averagetemperature", "veteranspercapita", "growthsince2010" , "density", "maxweeklybenefitamount"]]

# Remove "costindex"
new_df = df[["homelesscpt","householdincome", "percenthighschoolorhigher","percentbachelorsorhigher" ,"unemploymentrate", "averagetemperature", "veteranspercapita", "growthsince2010" , "density", "maxweeklybenefitamount"]]


# Calculate extra values (OPTIONAL)

print(new_df.head())

# EDA - correlation plot
# (new_df.corr()).to_csv("C:/Users/sykri/OneDrive/CSCI E-101/Final Project/new_df_corr.csv")
# print(sns.pairplot(new_df))
# plt.show()

# # VIF
# from statsmodels.tools.tools import add_constant
# new_df = add_constant(new_df)
# print(new_df.head(3))
#
# VIFvalue=variance_inflation_factor(new_df.values, 2)
# print(VIFvalue)
#
# VIFdf = pd.DataFrame()
# VIFdf["X_Variables"] = new_df.columns
#
# VIFdf["VIF_Values"] = [variance_inflation_factor(new_df.values, i)
#                        for i in range(len(new_df.columns))]
#
# VIFdf = VIFdf.drop(labels=range(0, 2), axis=0)
#
# print(VIFdf)

# ANOVA

# # Multiple regression on
results = ols ("homelesscpt ~ householdincome + percenthighschoolorhigher + "
                            "percentbachelorsorhigher + unemploymentrate + averagetemperature + "
                            "veteranspercapita + growthsince2010 + density + "
                            "maxweeklybenefitamount", data=new_df).fit()

# # Remove insignificant values percentbachelorsorhigher + unemploymentrate + averagetemperature + veteranspercapita + growthsince2010 +
# results = ols ("homelesscpt ~ householdincome + percenthighschoolorhigher + "
#                             "density + maxweeklybenefitamount", data=new_df).fit()

print(results.summary())
