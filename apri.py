#!/usr/bin/env python
# coding: utf-8

# In[24]:


get_ipython().system('pip install apyori')


# In[25]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori


# In[26]:


store_data = pd.read_csv('store_data.csv', header=None)


# In[27]:


store_data.head()


# ## convert our pandas dataframe into a list of lists

# In[28]:


records = []
for i in range(0, 7501):
    records.append([str(store_data.values[i,j]) for j in range(0, 20)])


# ## Apply Apriori
# ## min_support: to select the items with support values greater than it
# ## min_confidence: filters those rules that have confidence greater than the confidence threshold specified by it

# In[29]:


association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)


# In[34]:


# print(association_rules[0])
print(len(association_results))


# In[35]:


for item in association_results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")

