
# coding: utf-8

# input : k is the number of intersecting fair
# output : size of maximal subfamily guaranteed intersecting

# In[1]:

import math


# In[2]:

def ex(n,r):
    v = (1-1/(r-1)) * n * n / 2
    return int(v // 1)


# In[3]:

def Turan(n):
    for i in range(2,n+2):
        if i < 10:
            text = "r= %d," % i
        else:
            text = "r=%d," % i
        print(text,ex(n,i))


# In[4]:

Turan(12)


# In[5]:

def m(n):
    return int(n*(n-1)/2)


# In[6]:

def Table(n):
    for i in range(n,m(n)+1):
        temp = 0
        for j in range(2,n+2):
            if ex(n,j) < i :
                temp = j
        if i < 10:
            text = "k= %d," % i
        else:
            text = "k=%d," % i
        print(text,temp)


# In[7]:

Table(12)


# In[8]:

def table2(n):
    for i in range(n,m(n)+1):
        a = n ** 2
        b=a/(a-2*i)
        c = math.ceil(b)
        if i < 10:
            text = "e= %d," % i
        else:
            text = "e=%d," % i
        print(text,c)


# In[9]:

table2(6)


# In[ ]:



