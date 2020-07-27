# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 19:41:32 2020

@author: dzihan
"""
# In[1]:
class Myclass:
    common = 10
    def __init__ (self):
        self.myvariable = 3
    def myfunction (self, arg1, arg2):
        return self.myvariable
# Build a first instance
instance = Myclass()
print("instance.myfunction(1, 2)" , instance.myfunction(1, 2))
# In[2]:
instance2 = Myclass()
print("instance.common ",instance.common)
print("instance2.common ",instance2.common)
# In[3]:
Myclass.common = 30

print("instance.common ", instance.common)

print("instance2.common ", instance2.common)
# In[4]:
instance.common = 10
print("instance.common ", instance.common)

print("instance2.common " , instance2.common)
# In[5]:
Myclass.common = 50

print("instance.common ", instance.common)
print("instance2.common " , instance2.common)
# In[6]:
class AnotherClass (Myclass):
    # The "self" argument is passed automatically
    # and refers to the class's instance, so you can set
    # instance variables as above, but from within the class.
    def __init__ (self, arg1):
        self.myvariable = 3
        print (arg1)

instance = AnotherClass ("hello")
print("instance.myfunction (1, 2) " , instance.myfunction (1, 2))
# In[7]:
instance.test = 10
print("instance.test " , instance.test)
