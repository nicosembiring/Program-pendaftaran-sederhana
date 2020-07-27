# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:45:18 2020

@author: ACER
"""

# In[]

#JANGAN DI RUN

import logging
import random
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
                    
class Counter(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start
    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 1
        finally:
            self.lock.release()

def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug('Sleeping %0.02f', pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Done')

counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()

logging.debug('Waiting for worker threads')
main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
logging.debug('Counter: %d', counter.value)

# In[]

import threading 


def MyFunction(num1, num2):
	"""This is user defined thread function"""
	print ("Given numbers= %s, %s" %(num1, num2))
	print ("Result = %d" %(int(num1)+int(num2)))
	return


def Main():
	t = threading.Thread(
			target=MyFunction, 
			args=(12,13)
		)
	t.start()


if __name__ == '__main__':
	Main()
    
# In[]
#NO
    
import threading
import logging
import time


logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                   )


class ThreadWithArgs(threading.Thread):
    def __init__(self, 
                group=None, 
                target=None, 
                name=None,
                args=(), 
                kwargs=None, 
                verbose=None
                ):

        threading.Thread.__init__(self, 
                                group=group, 
                                target=target, 
                                name=name,
                                verbose=verbose
                                )
        
        self.args = args
        self.kwargs = kwargs
        return

    def run(self):
        logging.debug('This thread is running with %s and %s', self.args, self.kwargs)
        return


def Main():
    for x in range(5):
        myThread = ThreadWithArgs(
            args=(x,), 
            kwargs={'Country':'USA', 'Zip':'12345'}
        )
        myThread.start()
        time.sleep(1)


if __name__ == "__main__":
    Main()
    
# In[]
#NO

class PrimeNumber(threading.Thread):
    prime_numbers = {} 
    lock = threading.Lock()
    
    def __init__(self, number): 
        threading.Thread.__init__(self) 
        self.Number = number
        PrimeNumber.lock.acquire() 
        PrimeNumber.prime_numbers[number] = "None" 
        PrimeNumber.lock.release() 
 
    def run(self): 
        counter = 2
        res = True
        while counter*counter < self.Number and res: 
            if self.Number % counter == 0: 
               res = False 
            counter += 1 
        PrimeNumber.lock.acquire() 
        PrimeNumber.prime_numbers[self.Number] = res 
        PrimeNumber.lock.release() 
threads = [] 
while True: 
    input = long(raw_input("number: ")) 
    if input < 1: 
        break 
 
    thread = PrimeNumber(input) 
    threads += [thread] 
    thread.start() 
 
for x in threads: 
    x.join()

# In[]
#NO
# Gabisa di run eror line 177, benerin kalo bisa    
    
import threading 
 
class PrimeNumber(threading.Thread): 
  def __init__(self, number): 
    threading.Thread.__init__(self) 
    self.Number = number
 
  def run(self): 
    counter = 2 
    while counter*counter < self.Number: 
      if self.Number % counter == 0: 
        print ("%d is no prime number, because %d = %d * %d" % ( self.Number, self.Number, counter, self.Number / counter))
        return 
        counter += 1 
        print ("%d is a prime number" % self.Number)
threads = [] 
while True: 
    input = long(raw_input("number: ")) 
    if input < 1: 
        break 
 
    thread = PrimeNumber(input) 
    threads += [thread] 
    thread.start() 
 
for x in threads: 
    x.join()
    
# In[]

import time
import threading
from threading import Thread


def ThreadFunction(i):
    print("Thread %i going to sleep for 5 seconds." % i)
    time.sleep(5)
    print("Thread %i is awake now." % i)


def Main():
  for i in range(10):
      myThread = Thread(target=ThreadFunction, args=(i, ))
      myThread.start()
      print("Current Thread count: %i." % threading.active_count())
    
    
if __name__ == "__main__":    
  Main()
  
# In[]
  
import threading
import time


def HelloWorld():
	"""User defined Thread function"""
	print ("Hello World")
	return


def Main():
	threads = [] # Threads list needed when we use a bulk of threads
	print ("Program started.  This program will print Hello World five times...")
	for i in range(5):
		mythread = threading.Thread(target=HelloWorld)
		threads.append(mythread)
		time.sleep(2)
		mythread.start()
	print ("Done! Program ended")


if __name__ == "__main__":
	Main()
    
# In[]
    
import threading
import datetime


class myThread (threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter

    def run(self):
        print ("Starting " + self.name)
        print_date(self.name, self.counter)
        print ("Exiting " + self.name)

def print_date(threadName, counter):
    datefields = []
    today = datetime.date.today()
    datefields.append(today)
    print ("%s[%d]: %s" % ( threadName, counter, datefields[0] ))


# Create new threads
thread1 = myThread("Thread", 1)
thread2 = myThread("Thread", 2)


# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting the Program!!!")

# In[]

import threading
import time


def ThreadFunction():
	print (threading.currentThread().getName(), "Starting")
	time.sleep(2)
	print (threading.currentThread().getName(), "Exiting")


def Main():
	w = threading.Thread(target=ThreadFunction)
	w.start()


if __name__ == '__main__':
	Main()

# In[]

# JANGAN DI RUN

import random
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def student():
    """thread student function"""
    t = threading.currentThread()
    pause = random.randint(1,5)
    logging.debug('sleeping %s', pause)
    time.sleep(pause)
    logging.debug('ending')
    return

for i in range(3):
    t = threading.Thread(target=student)
    t.setDaemon(True)
    t.start()

main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug('joining %s', t.getName())
    t.join()
    
# In[]
#NO

from thread import start_new_thread

threadId = 1


def factorial(n):
   global threadId
   if n < 1:   # base case
       print ("%s: %d" % ("Thread", threadId ))
       threadId += 1
       return 1
   else:
       returnNumber = n * factorial( n - 1 )  # recursive call
       print(str(n) + '! = ' + str(returnNumber))
       return returnNumber

start_new_thread(factorial,(5, ))
start_new_thread(factorial,(4, ))

c = raw_input("Waiting for threads to return...\n")

# In[]

import time
from threading import Thread


def ThreadFunction(x):
    print ("sleeping 5 sec from thread %d" % x)
    time.sleep(5)
    print ("finished sleeping from thread %d" % x)

def Main():
  for i in range(10):
      myThread = Thread(target=ThreadFunction, args=(i,))
      myThread.start()
      
if __name__ == "__main__":
  Main()
  
# In[]
  
import threading


def MyFunction():
	"""This is a user defined function"""
	print ("Hello World")
	return


def Main():
	"""This is where we create a thread. 
	Target means run this function when a thread is initiated."""
	myThread = threading.Thread(target=MyFunction) 	
	myThread.start() 	# Starting a thread


if __name__ == '__main__':
	Main()
    
# In[]
#NO
    
import threading 
import time 


class AsyncWrite(threading.Thread):
  def __init__(self, text, out):
    threading.Thread.__init__(self)
    self.text = text
    self.out = out 

    
  def run(self):
    file = open(self.out, "a")
    file.write(self.text + '\n')
    file.close()
    time.sleep(2)
    print ("Done! Completed storing input in a file named " + self.out)


def Main():
  message = raw_input("Enter a string: ")
  bg = AsyncWrite(message, 'out.txt')
  
  bg.start()
  print ("Hold on, the program is generating a file")
  

if __name__ == '__main__':
  Main()
  
# In[]
  
import threading
import time


def MyThread(num1, num2):
	print ("Given Numbers: %s, %s" %(num1, num2))
	sum1= int(num1) + int(num2)
	print ("Result: %d" %sum1)
	return


def Main():
	threads = []
	for i in range(5):
		t = threading.Thread(target=MyThread, args=(10,20))
		threads.append(t)
		time.sleep(0.5)
		t.start()


if __name__ == '__main__':
	Main()
    
# In[]
    
import logging
import random
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s',
                    )

class ActivePool(object):
    def __init__(self):
        super(ActivePool, self).__init__()
        self.active = []
        self.lock = threading.Lock()
    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('Running: %s', self.active)
    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Running: %s', self.active)

def worker(s, pool):
    logging.debug('Waiting to join the pool')
    with s:
        name = threading.currentThread().getName()
        pool.makeActive(name)
        time.sleep(0.1)
        pool.makeInactive(name)

pool = ActivePool()
s = threading.Semaphore(2)
for i in range(4):
    t = threading.Thread(target=worker, name=str(i), args=(s, pool))
    t.start()
    
# In[]
    
## This function returns a list of all active threads. 


import threading


def Main():
	for thread in threading.enumerate():
	    print("Thread name is %s." % thread.getName())
	    

if __name__ == '__main__':
	Main()
    
# In[]
    
#Python multithreading example to demonstrate locking.
#1. Define a subclass using Thread class.
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
        print ("Starting " + self.name)
        # Acquire lock to synchronize thread
        threadLock.acquire()
        print_date(self.name, self.counter)
        # Release lock for the next thread
        threadLock.release()
        print ("Exiting " + self.name)

def print_date(threadName, counter):
    datefields = []
    today = datetime.date.today()
    datefields.append(today)
    print ("%s[%d]: %s" % ( threadName, counter, datefields[0] ))

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
for t in threads:
    t.join()
print ("Exiting the Program!!!")

# In[]

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
                    
def lock_holder(lock):
    logging.debug('Starting')
    while True:
        lock.acquire()
        try:
            logging.debug('Holding')
            time.sleep(0.5)
        finally:
            logging.debug('Not holding')
            lock.release()
        time.sleep(0.5)
    return
                    
def worker(lock):
    logging.debug('Starting')
    num_tries = 0
    num_acquires = 0
    while num_acquires < 3:
        time.sleep(0.5)
        logging.debug('Trying to acquire')
        have_it = lock.acquire(0)
        try:
            num_tries += 1
            if have_it:
                logging.debug('Iteration %d: Acquired',  num_tries)
                num_acquires += 1
            else:
                logging.debug('Iteration %d: Not acquired', num_tries)
        finally:
            if have_it:
                lock.release()
    logging.debug('Done after %d iterations', num_tries)


lock = threading.Lock()

holder = threading.Thread(target=lock_holder, args=(lock,), name='LockHolder')
holder.setDaemon(True)
holder.start()

worker = threading.Thread(target=worker, args=(lock,), name='Worker')
worker.start()

# In[]

import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def worker_with(lock):
    with lock:
        logging.debug('Lock acquired via with')
        
def worker_no_with(lock):
    lock.acquire()
    try:
        logging.debug('Lock acquired directly')
    finally:
        lock.release()

lock = threading.Lock()
w = threading.Thread(target=worker_with, args=(lock,))
nw = threading.Thread(target=worker_no_with, args=(lock,))

w.start()
nw.start()

# In[]

import os, re

received_packages = re.compile(r"(\d) received")
status = ("no response","alive but losses","alive")

for suffix in range(20,30):
   ip = "192.168.178."+str(suffix)
   ping_out = os.popen("ping -q -c2 "+ip,"r")
   print ("... pinging ",ip)
   while True:
      line = ping_out.readline()
      if not line: break
      n_received = received_packages.findall(line)
      if n_received:
         print (ip + ": " + status[int(n_received[0])])
         
# In[]
        
import os, re, threading

class ip_check(threading.Thread):
   def __init__ (self,ip):
      threading.Thread.__init__(self)
      self.ip = ip
      self.__successful_pings = -1
   def run(self):
      ping_out = os.popen("ping -q -c2 "+self.ip,"r")
      while True:
        line = ping_out.readline()
        if not line: break
        n_received = re.findall(received_packages,line)
        if n_received:
           self.__successful_pings = int(n_received[0])
   def status(self):
      if self.__successful_pings == 0:
         return "no response"
      elif self.__successful_pings == 1:
         return "alive, but 50 % package loss"
      elif self.__successful_pings == 2:
         return "alive"
      else:
         return "shouldn't occur"
received_packages = re.compile(r"(\d) received")

check_results = []
for suffix in range(20,70):
   ip = "192.168.178."+str(suffix)
   current = ip_check(ip)
   check_results.append(current)
   current.start()

for el in check_results:
   el.join()
   print ("Status from ", el.ip,"is",el.status())
   
# In[]
   
## This program creates a thread, 
## officially names it and 
## tries to print the name


import threading
import time


def ThreadFunction():
	print (threading.currentThread().getName(), "Starting")
	time.sleep(2)
	print (threading.currentThread().getName(), "Exiting")

def ServiceFunction():
	print (threading.currentThread().getName(), "Starting")
	time.sleep(3)
	print (threading.currentThread().getName(), "Exiting")


def Main():
	myThread = threading.Thread(
		name='Service Function', 
		target=ServiceFunction
	)
	w = threading.Thread(
		name='Thread function',
		target=ThreadFunction
	)
	w2 = threading.Thread(
		target=ThreadFunction
	)

	w.start()
	w2.start()
	myThread.start()


if __name__ == "__main__":
	Main()
    
# In[]
    
import threading

lock = threading.RLock()

print ('First try :', lock.acquire())
print ('Second try:', lock.acquire(0))

# In[]

import threading

lock = threading.Lock()

print ('First try :', lock.acquire())
print ('Second try:', lock.acquire(0))

# In[]

import threading
import logging
import time


logging.basicConfig(
	level=logging.DEBUG,
	format = '(%(threadName)-10s) %(message)s',
)


class MyThread(threading.Thread):
    def run(self):
        logging.debug('This thread is running')
        return

for x in range(5):
	z=MyThread()
	z.start()
	time.sleep(1)
    
# In[]
    
import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
                    
def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    logging.debug('wait_for_event starting')
    event_is_set = e.wait()
    logging.debug('event set: %s', event_is_set)

def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    while not e.isSet():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(t)
        logging.debug('event set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')


e = threading.Event()
t1 = threading.Thread(name='block', 
                      target=wait_for_event,
                      args=(e,))
t1.start()

t2 = threading.Thread(name='non-block', 
                      target=wait_for_event_timeout, 
                      args=(e, 2))
t2.start()

logging.debug('Waiting before calling Event.set()')
time.sleep(3)
e.set()
logging.debug('Event is set')

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
    
## This multithreading program prints output 
## of square and cube of a series of numbers


import time
import threading


def PrintSquare(numbers):
  print("Print squares")
  for n in numbers:
    time.sleep(0.2)
    print("Square", n*n)


def PrintCube(numbers):
  print("Print cubes")
  for n in numbers:
    time.sleep(0.2)
    print("Cube", n*n*n)


def Main():
	arr = [2,3,4,5]
	t = time.time()
	PrintSquare(arr)
	PrintCube(arr)
	t1=threading.Thread(Target=PrintSquare, args=(arr,))
	t2=threading.Thread(Target=PrintCube, args=(arr,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print("Program took", time.time()-t)


if __name__ == '__main__':
	Main()
    
# In[]
#NO
    
## Above program has been written using multithreading module 
## and the following one has been written in conventional 
## way where threading module hasnot been used.
## A comparison between the above and folling program 
## would help the readers understand the difference 
## a normal program and a thread program.


import time


def PrintSquare(num):
    print("Print squares of the given numbers")
    for n in numbers:
                time.sleep(0.2)
    print("Square", n*n)


def PrintCube(num):
    print("Print cubes of the given numbers")
    for n in numbers:
 time.sleep(0.2)
    print("Cube", n*n*n)


arr = [2,3,4,5]
t = time.time()
PrintSquare(arr)
PrintCube(arr)
print("Program took", time.time()-t)

# In[]

import threading
import time 
# global variable x
x = 0
 
def Tfunc(i,lock):
 lock.acquire()
 print('from thread %d' %i)
 lock.release()
 
 
 # creating a lock
lock = threading.Lock()
 
 # creating threads
t1 = threading.Thread(target=Tfunc, args=(1,lock,))
t2 = threading.Thread(target=Tfunc, args=(2,lock,))
 
 # start threads
t1.start()
t2.start()
 
 # wait until threads finish their job
t1.join()
time.sleep(5)
t2.join()

# In[]

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s',
                    )

def consumer(cond):
    """wait for the condition and use the resource"""
    logging.debug('Starting consumer thread')
    t = threading.currentThread()
    with cond:
        cond.wait()
        logging.debug('Resource is available to consumer')

def producer(cond):
    """set up the resource to be used by the consumer"""
    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Making resource available')
        cond.notifyAll()

condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition,))

c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start()

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
#NO

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
#NO
    
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
#NO

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

