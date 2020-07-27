# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:08:23 2020

@author: Arjun
"""


# In[Membuat Thread Untuk Menghitung Jumlah Sahabat]:

import threading

def hitungSahabat(n):
    
    
    if (n == 0):
        print("Jumlah Sahabat : %s , Kuranglah \n" %n)
        
        
    elif (n > 1 and n < 5) :
        print("Jumlah Sahabat : %s , Cari Lagi \n" %n)
        
        
    else :
        print("Jumlah Sahabat : %s , Perfect \n" %n)


m1 = threading.Thread(target=hitungSahabat,args=(0,))

m2 = threading.Thread(target=hitungSahabat,args=(3,))

m3 = threading.Thread(target=hitungSahabat,args=(7,))


m1.start()

m2.start()

m3.start()


# In[Menambahkan join()]:

from threading import Thread

from time import sleep


def function01(arg,name):

    for i in range(arg):

        print(name,'i---->',i,'\n')

        print (name,"arg---->",arg,'\n')

        sleep(1)


def test01():

    thread1 = Thread(target = function01, args = (10,'thread1', ))
    thread1.start()


    thread2 = Thread(target = function01, args = (10,'thread2', ))
    thread2.start()


    thread1.join()
    thread2.join()


    print ("thread finished...exiting")


test01()


# In[Contoh ThreadPoolExecutor]:

import concurrent.futures

import urllib.request


URLS = ['http://www.facebook.com/',
        
        'http://www.instagram.com/',
        
        'http://www.twitter.com/',
        
        'http://www.youtube.com/',
        
        'http://www.whatsapp.com/']


# Ambil satu halaman dan laporkan URL dan kontennya
def load_url(url, timeout):

    with urllib.request.urlopen(url, timeout=timeout) as conn:

        return conn.read()


# Kita dapat menggunakan pernyataan with untuk memastikan utas segera dibersihkan
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:

    
    # Mulai operasi pemuatan dan tandai setiap masa depan dengan URL-nya
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    
    
    for future in concurrent.futures.as_completed(future_to_url):
    
        url = future_to_url[future]
        
        try:
            data = future.result()
        
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        
        else:
            print('%r page is %d bytes' % (url, len(data)))


# In[Contoh Lainnya ThreadPoolExecutor Utas]:
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")


# In[ThreadPoolExecutor]:
import concurrent.futures


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"


    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")


    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))


# In[Thread Menggunakan FakeDatabase]:

class FakeDatabase:
    def __init__(self):
        self.value = 0


    def update(self, name):
        logging.info("Thread %s: starting update", name)

        local_copy = self.value

        local_copy += 1

        time.sleep(0.1)

        self.value = local_copy

        logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")


    database = FakeDatabase()


    logging.info("Testing update. Starting value is %d.", database.value)


    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)


    logging.info("Testing update. Ending value is %d.", database.value)



# In[Multithreading]:
from _thread import start_new_thread

from time import sleep


threadId = 1

waiting = 2 


def factorial(n):

    global threadId

    rc = 0

    
    if n < 1:   # base case
        print("{}: {}".format('\nThread', threadId ))

        threadId += 1

        rc = 1


    else:
        returnNumber = n * factorial( n - 2 )  # recursive call

        print("{} != {}".format(str(n), str(returnNumber)))

        rc = returnNumber

    
    return rc


start_new_thread(factorial, (5, ))

start_new_thread(factorial, (4, ))


print("Waiting for threads to return...")

sleep(waiting)


# In[Membuat kelas utas untuk mencetak tanggal]:

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


# In[Multithreading example for locking]:

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


# In[Antrian Prioritas Thread]: 

# modul Antrian Python menyediakan sinkronisasi, kelas antrian benang-aman, termasuk FIFO (first in first out) Antrian antrian, LIFO (bertahan, keluar pertama) LifoQueue antrian, dan PriorityQueue antrian prioritas. 

# Modul antrian metode yang umum digunakan:

# Queue.qsize () mengembalikan ukuran antrian
# Queue.empty () jika antrian kosong, kembali Benar, Salah dan sebaliknya
# Queue.full () Jika antrian penuh, kembali Benar, False dan sebaliknya
# Sesuai dengan ukuran dan maxsize Queue.full
# Queue.get ([blok [, batas waktu]]) Mendapat antrian, waktu tunggu tunggu
# Queue.get_nowait () bukan Queue.get (False)
# Queue.put (item) menulis antrian, batas waktu menunggu waktu
# Queue.put_nowait (item) cukup Queue.put (item, False)
# Queue.task_done () setelah selesainya pekerjaan, Queue.task_done () fungsi mengirimkan sinyal untuk tugas telah selesai antrian
# Queue.join () benar-benar berarti sampai antrian kosong, kemudian melakukan operasi lain

import threading

import time

from multiprocessing import Queue


exitFlag = 0


class myThread (threading.Thread):

    def __init__(self, threadID, name, q):

        threading.Thread.__init__(self)

        self.threadID = threadID

        self.name = name
        self.q = q
 
    
    def run(self):
    
        print ("Starting " + self.name)
        
        process_data(self.name, self.q)
        
        print ("Exiting " + self.name)


def process_data(threadName, q):

    while not exitFlag:

        queueLock.acquire()

        if not workQueue.empty():

            data = q.get()

            queueLock.release()

            print ("%s processing %s" % (threadName, data))


        else:

            queueLock.release()

        time.sleep(1)


threadList = ["Thread-1", "Thread-2", "Thread-3"]

nameList = ["One", "Two", "Three", "Four", "Five"]

queueLock = threading.Lock()

workQueue = Queue(10)

threads = []

threadID = 1


for tName in threadList:
    
    thread = myThread(threadID, tName, workQueue)
    
    thread.start()
    
    threads.append(thread)
    
    threadID += 1


queueLock.acquire()

for word in nameList:

    workQueue.put(word)


queueLock.release()


while not workQueue.empty():
    pass


exitFlag = 1


for t in threads:
   
    t.join()

print ("Exiting Main Thread")



# In[Menggunakan utas meningkatkan waktu eksekusi]:

from multiprocessing import Queue

import time

#First Method
def greet_them(people):
    
    for person in people:

        print("Hello Dear " + person + ". How are you?")

        time.sleep(0.5)


#Second Method
def assign_id(people):

    i = 1


    for person in people:

        print("Hey! {}, your id is {}.".format(person, i))

        i += 1

        time.sleep(0.5)


people = ['Arjun', 'Yuda', 'Firwanda', 'Boy', 'William']


t = time.time()


greet_them(people)


assign_id(people)


print("Woaahh!! My work is finished..")


print("I took " + str(time.time() - t))



# In[join() Method With Time]:

import threading


import time


def fun1(a):
    time.sleep(3)# complex calculation takes 3 seconds


thread1 = threading.Thread(target = fun1, args = (1, ))


thread1.start()


thread1.join()


print(thread1.isAlive())



# In[API untuk menelurkan banyak utas dalam suatu program]:

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


# In[Mencetak nama utas dan proses yang sesuai untuk setiap tugas]:

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



# In[Memahami konsep kondisi lomba]:

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



# In[Lock object]:

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



# In[secara serial,]:

import os

import time

import threading

import multiprocessing

 
NUM_WORKERS = 4
 

def only_sleep():
    """ Do nothing, wait for a timer to expire """

    print("PID: %s, Process Name: %s, Thread Name: %s" % (
        os.getpid(),

        multiprocessing.current_process().name, threading.current_thread().name))
    
    time.sleep(1)
 
 
def crunch_numbers():
    """ Do some computations """
    
    print("PID: %s, Process Name: %s, Thread Name: %s" % (
        os.getpid(),
        multiprocessing.current_process().name, threading.current_thread().name))
    
    x = 0
    
    while x < 10000000:
        x += 1



# In[Pengamatan Serial]:
        
start_time = time.time()

for _ in range(NUM_WORKERS):
    only_sleep()

end_time = time.time()


 
print("Serial time=", end_time - start_time)
 

# Run tasks using threads
start_time = time.time()

threads = [threading.Thread(target=only_sleep) for _ in range(NUM_WORKERS)]
[thread.start() for thread in threads]
[thread.join() for thread in threads]
end_time = time.time()
 

print("Threads time=", end_time - start_time)
 

# Run tasks using processes
start_time = time.time()
processes = [multiprocessing.Process(target=only_sleep()) for _ in range(NUM_WORKERS)]
[process.start() for process in processes]
[process.join() for process in processes]
end_time = time.time()
 

print("Parallel time=", end_time - start_time)


# In[]:
# thread.py
 
import time
import logging
import requests
 
 
class WebsiteDownException(Exception):
    pass
 
 
def ping_website(address, timeout=20):
    """
    Check if a website is down. A website is considered down 
    if either the status_code >= 400 or if the timeout expires
     
    Throw a WebsiteDownException if any of the website down conditions are met
    """
    try:
        response = requests.head(address, timeout=timeout)
        if response.status_code >= 400:
            logging.warning("Website %s returned status_code=%s" % (address, response.status_code))
            raise WebsiteDownException()
    except requests.exceptions.RequestException:
        logging.warning("Timeout expired for website %s" % address)
        raise WebsiteDownException()
         
 
def notify_owner(address):
    """ 
    Send the owner of the address a notification that their website is down 
     
    For now, we're just going to sleep for 0.5 seconds but this is where 
    you would send an email, push notification or text-message
    """
    logging.info("Notifying the owner of %s website" % address)
    
    time.sleep(0.5)
     
 
def check_website(address):
    """
    Utility function: check if a website is down, if so, notify the user
    """
    
    try:
        ping_website(address)
    
    
    except WebsiteDownException:
    
        
        notify_owner(address)
