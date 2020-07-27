# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:09:22 2020

@author: dzihan
"""
# In[1]:
try:
  print(x)
except:
  print("An exception occurred")
# In[2]:
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
# In[3]
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
# In[4]:
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
# In[5]:
try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()