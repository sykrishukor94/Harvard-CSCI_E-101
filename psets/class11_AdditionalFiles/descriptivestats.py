#!/usr/bin/env python
# coding: utf-8

# # Problem 1
# 
# ***Even though so far we have been doing procedural programming so far, we have been using classes, and objects indirectly. Think of the libraries pandas, numpy, and their function we have been using. They are all organized in classes, and we have been using them .***
# 
# *** Let's say you are a software engineer working for University XYZ. You are asked to create a module called descriptivestats that professors can use to get some statistics of the student grades. Perform the following task: ***
# 
# 1. Create a class called DescriptiveStats
# 2. The class should have the attribute X_list
# 3. The following methods:
# 
#     a. mean , that calculates the mean of X_list
#     
#     b. variance , that calculates the variance of X_list. Tt should calculate the sample variance by default
#     
#     c. std_dev , that calculates the std_dev of X_list 
# 
# 4. save the file as descriptivestats.py in the same folder as this notebook
# 
# 5. We will use your module that you created in the next task.
# 
# 
# Formulas you may need:
# 
# ### Mean
# $$ \bar{x} = \frac{\sum_{i=1}^{n}x_i}{n} $$
# 
# 
# ### Variance
# $$S^2 = \frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1} $$

# In[15]:


class DescriptiveStats:
    
    def __init__(self, X_list):
        #your code here
        self.__X_list = X_list
        
    
    def mean(self):
        #your code here
        sum =0
        for i in range(len(self.__X_list)):
            sum += self.__X_list[i]
        
        return sum/(len(self.__X_list))
    
    def variance(self):
        #your code here
        x_bar = self.mean()
        numerator = 0
        
        for i in range(len(self.__X_list)):
            numerator += (self.__X_list[i] - x_bar)**2
        
        return numerator / (len(self.__X_list)-1)
        
    
    
    # your code here for std_dev
    
    def std_dev(self):
        return (self.variance())**(1/2)
    


