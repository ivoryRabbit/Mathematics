
# coding: utf-8

# In[1]:

import numpy as np
# import matplotlib.pyplot as plt


# In[2]:

def KG(n):
    V = [[i+1, j+1] for i in range(n) for j in range(i+1, n)]
    E = []
    lenV = len(V)
    for i in range(lenV):
        for j in range(i+1, lenV):
            if set(V[i]) & set(V[j]) == set():
                E = E + [[V[i],V[j]]]
    
    return V, E


# In[5]:

V, E = KG(4)
print(V)
print(E)


# # This is the first time to use jupyter notebook

# In[ ]:



