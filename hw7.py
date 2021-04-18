#!/usr/bin/env python
# coding: utf-8

# In[24]:


# homework 7

import numpy as np
# import math
import matplotlib.pyplot as plt
import random


# In[25]:


# Q2.6 generate data

alist = []
for setnum in range(10000):
    a = 1
    for valnum in range(200):
        val = random.uniform(-1,1)
        if (val < a) and (val > 0):
            a = val
    alist.append(a/2)


# In[27]:


# Q2.6 histogram

n, bins, patches = plt.hist(x=alist, bins=50, rwidth=.85)


# In[29]:


# Q2.6 quantile
print("95% quantile:",np.quantile(alist,0.95))


# In[ ]:




