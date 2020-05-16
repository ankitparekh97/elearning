#!/usr/bin/env python
# coding: utf-8

# In[3]:


counter = 1
for i in range(5):    
    if(i == counter):        
        print ('*' * counter)
        counter +=1
        
for j in range(5,0,-1):    
    if(j == counter):        
        print ('*' * counter)
        counter -=1


# In[ ]:




