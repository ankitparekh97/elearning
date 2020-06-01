#!/usr/bin/env python
# coding: utf-8

# In[118]:


string = ['qwertyui','tyuio','qwetrsdfghjklzxcvbnpaqfldfg','asdfghjkl','mnbvcxz','plmnko','alskdjgh']
 
def longestWord(string):
    a = len(string)
    for i in range(len(string)):
        if(len(string[i]) >= a):
            a = len(string[i])
            b = string[i]
    return b    
    
            
x = longestWord(string)
print(x)


# In[ ]:





# In[ ]:




