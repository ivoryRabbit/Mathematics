#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def betti_number(facets):
    
    def make_subsets(List):
        upList = list()
        queue = [List]
        while queue:
            x = queue.pop()
            if x not in upList:
                upList.append(sorted(x))
            for i in range(len(x)):
                queue.append(x[:i]+x[i+1:])
        return upList
    
    def make_complex(facets):
        max_len = max([len(x) for x in facets])
        K = [[] for _ in range(max_len+1)]
        queue = [facet for facet in facets]
        while queue:
            face = queue.pop()
            if face not in K[len(face)]:
                K[len(face)].append(sorted(face))
            for i in range(len(face)):
                queue.append(face[:i]+face[i+1:])
        return K
    
    def make_chains(facets):
        K = make_complex(facets)
        chains = [make_subsets(face) for face in K][1:]
        for _ in range(2):
            chains.append([[]])
        return chains
    
    def boundary(sigma):
        result = list()
        for face in sigma:
            for i in range(len(face)):
                bd = sorted(face[:i] + face[i+1:])
                if not bd:
                    return result
                if bd in result:
                    result.remove(bd)
                else:
                    result.append(bd)
        return result
    
    def image(chain_left, chain_right):
        result = list()
        for sigma in chain_left:
            bd = boundary(sigma)
            if bd in chain_right and bd not in result:
                result.append(bd)
        return result
    
    def kernel(chain_left, chain_right):
        result = list()
        for sigma in chain_left:
            bd = boundary(sigma)
            if not bd:
                result.append(sigma)
        return result
    
    max_len = max([len(x) for x in facets])
    chains = make_chains(facets)
    betties = list()
    
    for k in range(max_len+1):
        z_k = len(kernel(chains[k], chains[k-1]))
        b_k = len(image(chains[k+1], chains[k]))
        betti_k = int(np.log2(z_k) - np.log2(b_k))
        betties.append(betti_k)
        print(f'betti_{k} = {betti_k}')
    return betties


# In[3]:


facets = [[1, 2], [2, 3], [3, 1]]
betti_number(facets)


# In[4]:


facets = [[1, 2, 3]]
betti_number(facets)


# In[5]:


facets = [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 5]]
betti_number(facets)


# In[ ]:


facets = [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [2, 3, 4, 5]]
betti_number(facets)


# In[ ]:




