#!/usr/bin/env python
# coding: utf-8

# In[151]:


string = ['pyfhdfg','mjuyqsddfsd','lkjfdqwsdfrt','pghkjghaghjfgg','zxvnsdfsdfsdf','fghadAsasa','mwersdfsd']
 
def longestWord(string):
    a = []
    for i in range(len(string)):
         a.append(len(string[i]))
    yield a
    
            
x = longestWord(string)

for a in x:
    print(a)


# In[ ]:


#program to return True if it is a vowel       


# In[155]:


def isVowel(i):
    vowel = ['a','e','i','o','u']
    for x in vowel:
        if(x == i):
            return True
        else:
            return False
        
        
check_vowel = isVowel('y')       
check_vowel


# In[ ]:




