# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 00:13:53 2020

@author: Sujadi
"""

# In[]

import threading
import time 


tLock = threading.Lock()


def timer(name, delay, repeat):
  print ("Timer: " + name + " Started")
  
  tLock.acquire()
  print (name + " has acquired lock")
  while repeat > 0:
    time.sleep(delay)
    print (name + ":" + str(time.ctime(time.time())))
    repeat -= 1
  print (name + "is releasing the lock")
  tLock.release()
  print ("Timer: " + name + "Completed")

  
def Main():
  thread1 = threading.Thread(
    target=timer, 
    args=("Timer1", 1, 5)
  )
  thread2 = threading.Thread(
    target=timer, 
    args=("Timer2", 2, 5)
  )
  thread1.start()
  thread2.start()

  print ("Main function completed")


if __name__ == '__main__':
  Main()
  
# In[]

import threading
import time


class MyThread(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))              # Thread-x started
        time.sleep(1)                                      
        print("{} finished!".format(self.getName()))             # Thread-x finished


def Main():
    for x in range(4):                                     
        mythread = MyThread(name = "Thread-{}".format(x + 1))  # Instantiate a thread and pass a unique ID to it
        mythread.start()
        time.sleep(1)   

        
if __name__ == '__main__':
	Main()  
    
# In[]

# Python program to illustrate the concept
# of threading
import threading
import os
 
def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))
 
def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))
 
if __name__ == "__main__":
 
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))
 
    # print name of main thread
    print("Main thread name: {}".format(threading.main_thread().name))
 
    # creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')  
 
    # starting threads
    t1.start()
    t2.start()
 
    # wait until all threads finish
    t1.join()
    t2.join()
    
# In[]
    
import random
import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def show_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value=%s', val)


def worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)

local_data = threading.local()
show_value(local_data)
local_data.value = 1000
show_value(local_data)

for i in range(2):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()
    
# In[]
    
import random
import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )


def show_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value=%s', val)

def worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)

class MyLocal(threading.local):
    def __init__(self, value):
        logging.debug('Initializing %r', self)
        self.value = value

local_data = MyLocal(1000)
show_value(local_data)

for i in range(2):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()
    
# In[]
    
import time
from threading import Thread

#create function for thread
def Tfunc(i):
 print("%d sleeping 5 sec from thread\n" % i)
 time.sleep(5)
 print("\n %d finished sleeping from thread" % i)

#start the thread for function
for i in range(5):
 t1 = Thread(target=Tfunc, args=(i,))
 t1.start()
 
# In[]
 
import threading
import time
import logging


def daemon():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')


def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

d = threading.Thread(name='daemon', target=daemon, daemon=True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# In[]

import threading
import time
import logging


def daemon():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')


def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

d = threading.Thread(name='daemon', target=daemon, daemon=True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# In[]

import threading
import time
import logging


def daemon():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')


def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

d = threading.Thread(name='daemon', target=daemon, daemon=True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join(0.1)
print('d.isAlive()', d.isAlive())

# In[]

import random
import threading
import time
import logging


def worker():
    """thread worker function"""
    pause = random.randint(1, 5) / 10
    logging.debug('sleeping %0.2f', pause)
    time.sleep(pause)
    logging.debug('ending')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

for i in range(3):
    t = threading.Thread(target=worker, daemon=True)
    t.start()

main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug('joining %s', t.getName())
    t.join()
    
# In[]
    
## A Timer starts its work after a delay, 
## and can be canceled at any point within that delay time period.


import threading
import time
import logging


logging.basicConfig(
	level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)


def delayed():
    logging.debug('Thread program still running')
    return

def Main():
	t1 = threading.Timer(3, delayed)
	t1.setName('Timer 1')
	t2 = threading.Timer(3, delayed)
	t2.setName('Timer 2')

	logging.debug('Starting thread timers')
	t1.start()
	t2.start()

	logging.debug('We are waiting before canceling %s', t2.getName())
	time.sleep(2)
	logging.debug('Now canceling %s', t2.getName())
	t2.cancel()


if __name__ == "__main__":
	Main()
    
# In[]
    
from threading import Thread 
import time 


def timer(name, delay, repeat):
  print ("Timer: " + name + " Started")
  
  while repeat > 0:
    time.sleep(delay)
    print (name + ":" + str(time.ctime(time.time())))
    repeat -= 1
  print ("Timer: " + name + "Completed")
  

def Main():
  thread1 = Thread(target=timer, args=("Timer1", 1, 5))
  thread2 = Thread(target=timer, args=("Timer2", 2, 5))
  thread1.start()
  thread2.start()
  
  print ("Main completed")
  
if __name__ == '__main__':
  Main()
  
# In[]
  
import time
import threading 

#create function for thread
def Tfunc(i):
 print("Thread no.:%d" % (i+1))
 time.sleep(5)
 print("%d finished sleeping from thread\n" % i)

#start the thread for function
for i in range(3):
 t1 = threading.Thread(target=Tfunc, args=(i,))
 t1.start()
 
#check thread is alive or not
 c=t1.isAlive()

#fetch the name of thread
 c1=t1.getName()
 print('\n',c1,"is Alive:",c)

#get toatal number of thread in execution
 count=threading.active_count()
 print("Total No of threads:",count)
 
# In[]
 
import requests
from multiprocessing.dummy import Pool
import time
from datadiff import diff

 
def getzip(code):
    try:
        code = str(code)
        url = "https://maps.googleapis.com/maps/api/geocode/json?address={}".format(code)
        res = requests.get(url).json()['results']
        if len(res) < 1: # Re-try
            print ("Retrying")
            return getzip(code)
        iszip = 'postal_code' in res[0]['types'] and "United States" in str(res[0]['address_components'])
    except Exception as e:
        print ("In error")
        print (e)
        iszip = False
    return (code, iszip)
ziprange = range(94400, 94420)
print ("Range is: " + str(len(ziprange)))
 
print ("Using one thread")
start = time.time()
syncres = [getzip(c) for c in ziprange] 
print ("took " + str(time.time() - start))
 
print ("Using multiple threads")
start = time.time()
 
# Magic
pool = Pool(10)
asyncres = pool.map(getzip, ziprange)
pool.close()
pool.join()
asyncres = sorted(asyncres)
# End of Magic
 
print ("took " + str(time.time() - start))
 
# Make sure results are equal
d = diff(syncres, asyncres)
if len(d.diffs) > 0:
    print ("diff is")
    print (d)
 
for r in asyncres:
    print ("Zip code {} is {} US code".format(r[0], "valid" if r[1] else "invalid"))
# In[]
# WEB BARU
# SEMANGAT YEY
    
import threading
import time



def sleeper(n, name):
    print('Hi, I am {}. Going to sleep for 5 seconds \n'.format(name))
    time.sleep(n)
    print('{} has woken up from sleep \n'.format(name))
    
    
    
    
t = threading.Thread(target = sleeper, name = 'thread1', args =(5, 'thread1') )
 
 
t.start()
 
 
 
t.join()
 
 
print('hello')
print('what is going on')

# In[]

#Using threading with queue

import queue
import threading
import time


def putting_thread(q):
    while True:
        print('starting thread')
        time.sleep(10)
        q.put(5)
        print('put something')
##        
#    
#        
#
q = queue.Queue()
t = threading.Thread(target = putting_thread, args = (q,),daemon = True)
t.start()

q.put(5)



print(q.get())
print('first item gotten')
print(q.get())
print('finished')


#intializing a variable to q.get()

x =q.get()

print(x)



#difference between LIFO and FIFO


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
    
# In[]
    
import os
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import time
import queue
from threading import Thread




SAVE_DIR = r'E:\Kuliah\Semester 6\Sistem Tersebar'



def decorator_function(func):
    def wrapper(*args,**kwargs):
        session = requests.Session()
        retry = Retry(connect=0, backoff_factor=0.2)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        return func(*args, session = session, **kwargs)
    return wrapper








#Using threading:
image_count = 0

#optional decorator_function
#@decorator_function   
def download_image(SAVE_DIR,q, session = None):
        global image_count
        if not session:
                session = requests.Session()
        while not q.empty():
            
            try:

                    r = session.get(q.get(block = False))

            except (requests.exceptions.RequestException, UnicodeError) as e:
                print(e)
                image_count += 1
                q.task_done()
                continue

            image_count += 1
            q.task_done()

            print('image', image_count)
            with open(os.path.join(
                        SAVE_DIR, 'image_{}.jpg'.format(image_count)),
                        'wb') as f:

                f.write(r.content)
                
               

q =queue.Queue()
with open(r'E:\Kuliah\Semester 6\Sistem Tersebar\tes.txt', 'rt') as f:
    for i in range(200):
        line = f.readline()
        q.put(line.strip())
print(q.qsize())


threads = []
start = time.time()
for i in range(20):
     t = Thread(target = download_image, 
                args = (SAVE_DIR,q))
     #t.setDaemon(True)
     threads.append(t)
     t.start()
q.join()

for t in threads:
    t.join()
    print(t.name, 'has joined')

end = time.time()
print('time taken: {:.4f}'.format(end - start))


#time taken: 7.4640
#time taken: 5.0860

# In[]


import threading
import time



def sleeper(n, name):
    print('Hi, I am {}. Going to sleep for 5 seconds \n'.format(name))
    time.sleep(n)
    print('{} has woken up from sleep \n'.format(name))
    
    
    
    
t = threading.Thread(target = sleeper, name = 'thread1', args =(5, 'thread1') )
 
 
t.start()
 
 
 
t.join()
 
 
print('hello')
print('what is going on')

# In[]

import threading
import time



def sleeper(n, name):
    print('Hi, I am {}. Going to sleep for 5 seconds \n'.format(name))
    time.sleep(n)
    print('{} has woken up from sleep \n'.format(name))
    
    
 
start = time.time()
threads = []

for i in range(5):
    t = threading.Thread(target = sleeper, name = 'thread{}'.format(i), args =(5,'thread{}'.format(i) ) )
    threads.append(t)
    t.start()
    print('{} has started \n'.format(t.name))
 
 
 
    
for i in threads:

    i.join()
    
end = time.time()



print('time is {}'.format(end - start))






#example 2 without threads


import time

def sleeper(n, i):
    print ('Hi, I am function {}. Going to sleep for 5 seconds \n'.format(i))
    time.sleep(n)
    print('function{} has woken up from sleep \n'.format(i))




start = time.time()

for i in range(5):
    print('{} has started \n'.format(i))
    x = sleeper(5, i)
    
    
end  = time.time()


print('time taken: {}'.format(end - start))

# In[]
# BARU LAGI YAA
#SABARR

import threading

localSchool = threading.local()


def processStudent():
    std = localSchool.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def processThread(name):
    localSchool.student = name
    processStudent()

t1 = threading.Thread(target=processThread, args=('Alice', ), name='T-a')
t2 = threading.Thread(target=processThread, args=('Bob', ), name='T-b')

t1.start()
t2.start()

t1.join()
t2.join()
    
# In[]

import time, threading


balance = 0
lock = threading.Lock()

def change_it(n):

    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# In[]

# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading 
  
def print_cube(num): 
    """ 
    function to print cube of given num 
    """
    print("Cube: {}".format(num * num * num)) 
  
def print_square(num): 
    """ 
    function to print square of given num 
    """
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=print_square, args=(10,)) 
    t2 = threading.Thread(target=print_cube, args=(10,)) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!") 
    
# In[]
    
# Python program to illustrate the concept 
# of threading 
import threading 
import os 
  
def task1(): 
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name)) 
    print("ID of process running task 1: {}".format(os.getpid())) 
  
def task2(): 
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name)) 
    print("ID of process running task 2: {}".format(os.getpid())) 
  
if __name__ == "__main__": 
  
    # print ID of current process 
    print("ID of process running main program: {}".format(os.getpid())) 
  
    # print name of main thread 
    print("Main thread name: {}".format(threading.current_thread().name)) 
  
    # creating threads 
    t1 = threading.Thread(target=task1, name='t1') 
    t2 = threading.Thread(target=task2, name='t2')   
  
    # starting threads 
    t1.start() 
    t2.start() 
  
    # wait until all threads finish 
    t1.join() 
    t2.join() 
    
# In[]
    
import threading 
  
# global variable x 
x = 0
  
def increment(): 
    """ 
    function to increment global variable x 
    """
    global x 
    x += 1
  
def thread_task(): 
    """ 
    task for thread 
    calls increment function 100000 times. 
    """
    for _ in range(100000): 
        increment() 
  
def main_task(): 
    global x 
    # setting global variable x as 0 
    x = 0
  
    # creating threads 
    t1 = threading.Thread(target=thread_task) 
    t2 = threading.Thread(target=thread_task) 
  
    # start threads 
    t1.start() 
    t2.start() 
  
    # wait until threads finish their job 
    t1.join() 
    t2.join() 
  
if __name__ == "__main__": 
    for i in range(10): 
        main_task() 
        print("Iteration {0}: x = {1}".format(i,x)) 
        
# In[]
        
import threading 
  
# global variable x 
x = 0
  
def increment(): 
    """ 
    function to increment global variable x 
    """
    global x 
    x += 1
  
def thread_task(lock): 
    """ 
    task for thread 
    calls increment function 100000 times. 
    """
    for _ in range(100000): 
        lock.acquire() 
        increment() 
        lock.release() 
  
def main_task(): 
    global x 
    # setting global variable x as 0 
    x = 0
  
    # creating a lock 
    lock = threading.Lock() 
  
    # creating threads 
    t1 = threading.Thread(target=thread_task, args=(lock,)) 
    t2 = threading.Thread(target=thread_task, args=(lock,)) 
  
    # start threads 
    t1.start() 
    t2.start() 
  
    # wait until threads finish their job 
    t1.join() 
    t2.join() 
  
if __name__ == "__main__": 
    for i in range(10): 
        main_task() 
        print("Iteration {0}: x = {1}".format(i,x)) 
        
# In[]
        
import logging
import threading
import time

def thread_func(name):
     logging.info("Thread %s: starting...",name)
     time.sleep(2)
     logging.info("Thread %s: finishing...",name)

if __name__ == "__main__":
     format = "%(asctime)s: %(message)s"
     logging.basicConfig(format=format,level=logging.INFO,
                         datefmt="%H:%M:%S")
     logging.info("Main    : before creating thread...")
     t = threading.Thread(target=thread_func,args=(1,))
     logging.info("Main    : before running thread...")
     t.start()
     logging.info("Main    : wait for the thread to finish...")
     # t.join()
     logging.info("Main    : all done...")
     
# In[]

#Python multithreading example.
#1. Calculate factorial using recursion.
#2. Call factorial function using thread. 

from _thread import start_new_thread
from time import sleep

threadId = 1 # thread counter
waiting = 2 # 2 sec. waiting time

def factorial(n):
    global threadId
    rc = 0
    
    if n < 1:   # base case
        print("{}: {}".format('\nThread', threadId ))
        threadId += 1
        rc = 1
    else:
        returnNumber = n * factorial( n - 1 )  # recursive call
        print("{} != {}".format(str(n), str(returnNumber)))
        rc = returnNumber
    
    return rc

start_new_thread(factorial, (5, ))
start_new_thread(factorial, (4, ))

print("Waiting for threads to return...")
sleep(waiting)

# In[]
        
#Python multithreading example to print current date.
#1. Define a subclass using threading.Thread class.
#2. Instantiate the subclass and trigger the thread.

import threading
import datetime

class myThread (threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    def run(self):
        print("\nStarting " + self.name)
        print_date(self.name, self.counter)
        print("Exiting " + self.name)

def print_date(threadName, counter):
    datefields = []
    today = datetime.date.today()
    datefields.append(today)
    print("{}[{}]: {}".format( threadName, counter, datefields[0] ))

# Create new threads
thread1 = myThread("Thread", 1)
thread2 = myThread("Thread", 2)

# Start new Threads
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("\nExiting the Program!!!")

# In[]

#Python multithreading example to demonstrate locking.
#1. Define a subclass using threading.Thread class.
#2. Instantiate the subclass and trigger the thread. 
#3. Implement locks in thread's run method. 

import threading
import datetime

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    def run(self):
        print("\nStarting " + self.name)
        # Acquire lock to synchronize thread
        threadLock.acquire()
        print_date(self.name, self.counter)
        # Release lock for the next thread
        threadLock.release()
        print("Exiting " + self.name)

def print_date(threadName, counter):
    datefields = []
    today = datetime.date.today()
    datefields.append(today)
    print("{}[{}]: {}".format( threadName, counter, datefields[0] ))

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread("Thread", 1)
thread2 = myThread("Thread", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("\nExiting the Program!!!")

# In[]

import time
from threading import Thread

def sleepMe(i):
    print("Thread %i going to sleep for 5 seconds." % i)
    time.sleep(5)
    print("Thread %i is awake now." % i)

for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()

# In[]
    
import time
import threading
from threading import Thread

def sleepMe(i):
    print("Thread %i going to sleep for 5 seconds." % i)
    time.sleep(5)
    print("Thread %i is awake now." % i)

for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()
    print("Current Thread count: %i." % threading.active_count())
    
# In[]
    
import threading

def delayed():
    print("I am printed after 5 seconds!")

thread = threading.Timer(3, delayed)
thread.start()

# In[]

import threading
for thread in threading.enumerate():
    print("Thread name is %s." % thread.getName())
    
# In[]
    

import time
import threading 
from threading import Thread

def sleepMe(i):
    print("Thread %s going to sleep for 5 seconds." % threading.current_thread())
    time.sleep(5)
    print("Thread %s is awake now.\n" % threading.current_thread())

#Creating only four threads for now
for i in range(4):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()