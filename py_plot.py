#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import sys

read = pd.read_csv(sys.argv[1])
read

df = pd.read_csv("regrex1.csv")
df.plot(kind='scatter',x='x',y='y')


# In[7]:
read = pd.read_csv(sys.argv[1])
read.plot.scatter(x = 'x', y = 'y')
plt.savefig('py_orig.png')


#create basic scatterplot
plt.plot(df.x, df.y, 'o')


#obtain m (slope) and b(intercept) of linear regression line
m, b = np.polyfit(df.x, df.y, 1)

#add linear regression line to scatterplot 
plt.plot(df.x, m*df.x+b)

plt.savefig('py_lm.png')


# In[ ]:




