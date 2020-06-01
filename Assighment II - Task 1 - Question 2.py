#!/usr/bin/env python
# coding: utf-8

# In[38]:


x = [i for i in ['A', 'C', 'A', 'D', 'G', 'I', 'L', 'D']]
print(x)


# In[46]:


b = []
cnt= 1
for i in ['x','y','z']:
   b.append(i)
   b.append(i + i)
   b.append(i + i + i)
   b.append(i + i + i + i)
   cnt += 1    
   
print(b) 


# In[61]:


b = []
for i in ['2','3','4']:
    b.append(list(i))
    
print(b) 


# In[ ]:




