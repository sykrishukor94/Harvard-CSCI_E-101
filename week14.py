# Week 14 Lecture Code
# import packages
#
import pandas as pd

# need for regression analysis
from statsmodels.formula.api import ols

# VIF for Multicollinearity Testing
from statsmodels.stats.outliers_influence import variance_inflation_factor

# read data from excel to dataframe variable
df = pd.read_excel("footballpunts.xlsx")

results = ols ("Distance ~ Hang + R_Strength", data=df).fit()
print(results.summary())

df.corr()


from statsmodels.tools.tools import add_constant
df = add_constant(df)
print(df.head(3))

VIFvalue=variance_inflation_factor(df.values, 2)
print(VIFvalue)

for i in range(len(df.columns)):
    print(variance_inflation_factor(df.values, i))

# Make it prettier w/ labels
VIFdf = pd.DataFrame()
VIFdf["X_Variables"] = df.columns

VIFdf["VIF_Values"] = [variance_inflation_factor(df.values, i)
                       for i in range(len(df.columns))]

print(VIFdf)

# Remove variables in range 0-2
VIFdf = pd.DataFrame()
VIFdf["X_Variables"] = df.columns

VIFdf["VIF_Values"] = [variance_inflation_factor(df.values, i)
                       for i in range(len(df.columns))]

VIFdf = VIFdf.drop(labels=range(0, 2), axis=0)

print(VIFdf)

# Drop variables w/ score >5 for multicollinearity, starting w/ highest