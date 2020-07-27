# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 21:05:28 2020

@author: FAHMI-PC
"""

#%% Exceptions
def one_function():
    try:
        # Division by zero causes one exception
        10/0
    except ZeroDivisionError:
        print("Oops, error.")
    else:
        # There was no exception, we can continue.
        pass
    finally:
        # This code is executed when the block
        # try..except is already executed and all exceptions
        # have been managed, even if a new one occurs
        # exception directly in the block.
        print("We finished.")
        
one_function()
        
#%% Importing libraries

import random
randomint = random.randint(1, 101)

print(randomint)

#%% Managing files

f = open ('test.txt', 'w') # open the file for writing
f.write ('Muhammad ') # write a line in file
f.write ('Fahmi') # write another line in file
f.close () # we close the file
f = open ('test.txt') # reopen the file for reading
content = f.read () # read all the contents of the file

print (content)

f.close() #close the file

#%% List comprehensions

#list comprehensions using strings
list_comprehension_1 = [ x for x in 'python parallel programming cookbook!' ]
print( list_comprehension_1)

#%%list comprehensions using numbers
l1 = [1,2,3,4,5,6,7,8,9,10]
list_comprehension_2 = [ x*10 for x in l1 ]
print( list_comprehension_2)

#%% Running Python scripts

python my_pythonscript.py

#%%



#%%
