#!/usr/bin/env python
# coding: utf-8

# # Area of Triangle (1.1)

# In[99]:


class Length:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def length(self):   
        length = (self.a + self.b + self.c) / 2
        return length
    
class Area(Length):
    def __init__(self,f,g,h):
        super().__init__(a,b,c)
           
    def area(self):
        length = super().length()
        a = self.a
        b = self.b
        c = self.c
        area = (length*(length-a)*(length-b)*(length-c)) ** 0.5
        return area
    
    
a = int(input('Enter First side of triangle\n'))
b = int(input('Enter Second side of triangle\n'))
c = int(input('Enter Third side of triangle\n'))

area = Area(a,b,c)
areaOfTriangle = area.area()
print(areaOfTriangle)    


# In[ ]:





# # filter_long_words (1.2)

# In[20]:


def filter_long_words(words,n):
    a = len(words)
    b = []
    for i in range(a):        
        if(len(words[i]) > n):
            b.append(words[i])
    return b
        
        
            
word = ['qwe','uwerww','irtyr']
n = 3

longest_words = filter_long_words(word,n)   
print(longest_words)


# In[ ]:




