# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:42:39 2020

@author: dzihan
"""




import threading
import time





def sleeper(n, name):
    print('hay, aku yang {}. Bentar lagi bobo 5 seconds... \n'.format(name))
    time.sleep(n)
    print('{} dah bangun nih \n'.format(name))
    
    
    


    
t = threading.Thread(target = sleeper, name = 'kesatu', args =(5, 'kedua') )


 
 
t.start()


 
 
 
t.join()
 



 
print('sampurasun')
print('corona pergi')

# In[3]:shuffle the data, split into 80% train, 20% 




import threading
import time








def sleeper(n, name):
    print('hayy aku yang {}. bentar lagi mau bobo 5 seconds... \n'.format(name))
    time.sleep(n)
    print('{} dah bangun nih \n'.format(name))
    
    
 




start = time.time()
threads = []








for i in range(5):
    t = threading.Thread(target = sleeper, name = 'kesatu{}'.format(i), args =(5,'kedua{}'.format(i) ) )
    threads.append(t)
    t.start()
    print('{} gass kuy \n'.format(t.name))
 
 
 
    




for i in threads:

    i.join()
    









end = time.time()

# In[2] 








import threading
import time





total = 4







def creates_items():
    global total
    for i in range(10):
        time.sleep(2)
        print('tambah bang')
        total += 1
    print('udah bang')










def creates_items_2():
    global total
    for i in range(7):
        time.sleep(1)
        print('tambah bang')
        total += 1
    print('nuhun bang')








def limits_items():
    
    

    



    global total
    while True:
        if total > 5:

            print ('kepenuhan')
            total -= 3
            print('kurangin ya 3')
        else:
            time.sleep(1)
            print('antosan kedap')






creator1 = threading.Thread(target  = creates_items)
creator2 = threading.Thread(target = creates_items_2)
limitor = threading.Thread(target = limits_items, daemon = True)

print(limitor.isDaemon())




creator1.start()
creator2.start()
limitor.start()




creator1.join()
creator2.join()
# In[0] 



import queue
import threading
import time




def nih_thread(q):
    while True:
        print('hayuu thread')
        time.sleep(10)
        q.put(5)
        print('nih something')
##        
#    
#        
#







q = queue.Queue()
t = threading.Thread(target = nih_thread, args = (q,),daemon = True)
t.start()

q.put(5)





print(q.get())
print('yeay something')
print(q.get())
print('alhamdulillah')


#intializing a variable to q.get()




x =q.get()



print(x)



#difference between LIFO and FIFO

# In[9]






import queue
q = queue.Queue()




for i in range(5):
    q.put(i)
    




while not q.empty():
    print(q.get(), end = '   ')
    
    



print('\n')    
    
    





import queue
q = queue.LifoQueue()

for i in range(5):
    q.put(i)
    
while not q.empty():
    print(q.get(), end = '   ')
    
    
    
    
# priority queue




import queue
import time







q = queue.PriorityQueue()

q.put((1, 'Priority 1'))
q.put((3, 'Prioirty 3'))
q.put((4 ,'Priority 4'))
q.put((2 ,'Priority 2'))





for i in range(q.qsize()):
    print(q.get()[1])
    
# In[8]




import threading
import time


total = 4






def creates_items():
    global total
    for i in range(10):
        time.sleep(2)
        print('nih item')
        total += 1
    print('udah nih')







def creates_items_2():
    global total
    for i in range(7):
        time.sleep(1)
        print('nih item')
        total += 1
    print('udah nih')






def limits_items():
    

    



    global total
    while True:
        if total > 5:

            print ('gakuat')
            total -= 3
            print('kurangin ya 3')
        else:
            time.sleep(1)
            print('antosan kedap')






creator1 = threading.Thread(target  = creates_items)
creator2 = threading.Thread(target = creates_items_2)
limitor = threading.Thread(target = limits_items, daemon = True)



print(limitor.isDaemon())




creator1.start()
creator2.start()
limitor.start()


creator1.join()
creator2.join()




print('dapet segini nih' , total)