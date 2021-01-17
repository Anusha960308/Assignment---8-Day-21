#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import Counter 
  
 
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red'] 
col_count = Counter(z) 
print(col_count) 
  
col = ['blue','red','yellow','green'] 
  
 
for color in col: 
    print (color, col_count[color])


# In[2]:


from collections import Counter 
  
coun = Counter(a=1, b=2, c=3) 
print(coun) 
  
print(list(coun.elements()))


# In[3]:


from collections import Counter 
  
coun = Counter(a=1, b=2, c=3, d=120, e=1, f=219) 
  
 
for letter, count in coun.most_common(3): 
    print('%s: %d' % (letter, count))


# In[ ]:




