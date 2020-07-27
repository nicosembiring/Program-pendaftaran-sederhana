


def run(self):
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs








import time
import threading





class BuatThread(threading.Thread):


    def run(self):
        print('{} gasss!'.format(self.getName()))
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs
        print('{} saur euy!'.format(self.getName()))
        



def sleepy (n, name) :
    print('Hi, I am {}. mau bobo 5 detik\
          \n'.format(name))
    time.sleep(n)
    print('{} gugah bobo \n'.format(name))
    
    
    


for i in range(4):
    t = BuatThread(target = sleepy, 
                 name = 'thread {}'.format(i+1),
                 args = (3, 'thread {}'.format(i+1)))



    t.start()

# In[2] 







import time
import threading

class BuatThread(threading.Thread):
    def __init__(self, number, func, args):
        threading.Thread.__init__(self)
        self.number = number
        self.func = func
        self.args = args
        
        
        
        
    def run(self):
        print('thread {} gasss '.format(self.number))
        self.func(*self.args)
        print('thread {} udahan '.format(self.number))
        
        
        
        
        
        
def double(number, cycles):
    for i in range(cycles):
        number += number
    print(number)
    
    
    
    
threads_list = []



for i in range(50):
    t = BuatThread(number = i +1, func = double, 
                 args = [i, 3])
    threads_list.append(t)
    t.start()



    
for t in threads_list:
    t.join()

# In[1] 
    
    
    
import threading
import time




class BuatThread(threading.Thread):
    def __init__(self, number, style, *args, **kwargs):
        super(BuatThread, self).__init__(*args, **kwargs)
        self.number = number
        self.style = style



        
        
    def run(self, *args, **kwargs):
        print('gaass')
        super(BuatThread, self).run(*args, **kwargs)
        print('udahan ah')
        


        
        
def sleeper (num, style):
    print('bobo dulu {} bentar as {}'.format(num, style))
    time.sleep(num)   





t = BuatThread(number =3, style = 'yellow', target = sleeper, 
             args = [3, 'yellow']) 




t.start()