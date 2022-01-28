# Week 13 Lecture code

import pandas as pd

# For oneway ANOVA
import scipy.stats as st

# For Post Hoc
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison as multi

# Read data stored in csv file
df = pd.read_csv("C:/Users/sykri/OneDrive/CSCI E-101/Week 13/differences3.csv")


# # assign label to each student type: Online, InPerson, Hybrid
df["Student"].replace({1:"Online", 2:"InPerson", 3:"Hybrid"}, inplace=True)

# Oneway ANOVA
Results = st.f_oneway(df["Score"][df["Student"]=="Online"], df["Score"][df["Student"]=="InPerson"], df["Score"][df["Student"]=="Hybrid"])

print ("ANOVA Results: ", Results)

# Post Hoc
MultiComp = multi(df["Score"], df["Student"])
PostHoc = MultiComp.tukeyhsd()

print (PostHoc)