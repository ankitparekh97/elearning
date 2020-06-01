#!/usr/bin/env python
# coding: utf-8

# In[61]:


from functools import reduce

def calculateCum(i,j):
    k = i * j
    return k
 
    
a = [1,2,3,4,5,6,7,8,9,10,11,12]   
x = reduce(calculateCum, a)
print(x)

y = reduce(lambda f,g : g - f, a)
y
 


# In[ ]:




