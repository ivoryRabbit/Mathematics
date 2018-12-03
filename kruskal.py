
# coding: utf-8

# In[1]:

import math


# In[2]:

import numpy


# In[105]:

def factorial(n,k):
    N = 1
    for i in range(k-1,n):
        N = N * (i+1)
    return N


# In[106]:

factorial(4,4)


# In[107]:

def binom(n,k):
    if n < k :
        return 0
    else:
        A = factorial(n,n-k+1)
        B = factorial(k,1)
    return int(A/B)


# In[108]:

binom(5,2)


# In[287]:

def cascade(n,k):
    if binom(n,k) == n:
        return (n,k)
    for i in range(1,n+k+1):
        if binom(i,k) > n:
            N = i-1
            break
    return N,k


# In[288]:

cascade(1000,6)


# In[289]:

binom(12,6)


# In[290]:

1000-924


# In[291]:

cascade(76,5)


# In[292]:

binom(8,5)


# In[293]:

1000-924-56


# In[294]:

cascade(20,4)


# In[295]:

binom(6,4)


# In[296]:

1000-924-56-15


# In[297]:

cascade(5,3)


# In[298]:

binom(4,3)


# In[299]:

1000-924-56-15-4


# In[300]:

cascade(1,2)


# In[303]:

def kruskal(n,k):
    if n < k:
        return "no kruskal"
    L = [n,k]; temp = []
    while n > 0:
        temp += [cascade(n,k)]
        n1 = cascade(n,k)[0]
        n = n - binom(n1,k)
        k = k-1
    return temp


# In[304]:

kruskal(1000,6)


# In[309]:

def kantona(n,k):
    L = kruskal(n,k)
    l = len(L)
    value = 0
    for i in range(l):
        value += binom(L[i][0],L[i][1]-1)
    return value


# In[310]:

kantona(1000,6)


# In[311]:

kantona(890,5)


# In[312]:

kantona(571,4)


# In[313]:

kantona(255,3)


# In[314]:

kantona(75,2)


# In[315]:

kantona(13,1)


# In[319]:

cascade(1000,6)


# In[320]:

binom(12,6)


# In[321]:

binom(13,6)


# In[322]:

binom(13,5)


# In[323]:

bool(890*1716 > 1000*1287)


# In[ ]:



