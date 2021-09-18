#!/usr/bin/env python
# coding: utf-8

# #1

# In[2]:


project = 'cake'


# In[3]:


difficulty = 4


# In[6]:


ingredients = ['flour', 'butter',
'sugar', 'eggs', 'cocoa powder', 'baking powder']


# In[7]:


print('apples' in ingredients)


# In[8]:


print('butter' in ingredients)


# In[11]:


print(('eggs' in ingredients) or ('margarine' in ingredients))


# In[12]:


print(('eggs' in ingredients) and ('margarine' in ingredients))


# In[14]:


flour = 175
butter = 175
sugar = '100g'
eggs = 2
cocoa_powder = '1ts'
baking_powder = 0.5


# In[17]:


print(type(flour))
print(type(butter))
print(type(sugar))
print(type(eggs))
print(type(cocoa_powder))
print(type(baking_powder))


# In[18]:


print('flour-',flour)
print('butter-',butter)
print('sugar-',sugar)
print('eggs-',eggs)
print('cocoa_powder-',cocoa_powder)
print('baking_powder-',baking_powder)


# #2

# In[19]:


a, b, c = 15, 8, 2


# In[25]:


5 * a**2 - a * b + (a%2) - a/5


# In[26]:


b**3 + 3*a*b - 10*c

