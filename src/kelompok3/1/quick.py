#%% -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:53:35 2020

@author: ROG
"""

#%%
x = 2
if x > 5:
	print("Nilai %d adalah besar dari 5" % x )
else :
	print("Nilai %d adalah kecil dari 5" % x)
#%%
variable = 3
variable += 2
print(variable)

_string_ = "Hello"
_string_ += " Parallel Programming CookBook Second Edition!"
print (_string_)

#%%let's play with lists
list_1 = [1, ["item_1", "item_1"], ("a", "tuple")]
list_2 = ["item_1", -10000, 5.01]

print(list_1)
print(list_1[2])
print(list_2[0])
print(list_2[2])
#%%
dictionary = {"Key 1": "item A", "Key 2": "item B", 3: 1000}
print(dictionary)
print(dictionary["Key 1"])
print(dictionary["Key 2"])
print(dictionary[3])
#%%
list_3 = ["Hello", "Ruvika", "how" , "are" , "you?"]
print(list_3[0:5])
print(list_3[0:1])
print(list_3[2:6])

