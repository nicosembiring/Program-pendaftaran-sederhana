# In[1]:

from threading import Thread
import math
import numpy as np
import time
import threading

Training_data = []
Testing_data = []

least_distance = 0
class_index = None

matrix_dimensions_row = None
matrix_dimensions_column = None

cosine_similarity_index = 0
num_of_threads = 0

Final_minimum_distance_and_index = {"min_dist":0,"min_index":0}

write_lock = threading.Lock()

def Take_input():
    global matrix_dimensions_row
    global matrix_dimensions_column
    global num_of_threads
    
    matrix_dimensions_row = int(input("Masukkan nomor baris N : "))
    matrix_dimensions_column = int(input("Masukkan nomor kolom M : "))
    num_of_threads = int(input("Masukkan nomor Threads ke : "))
    print("Generating a 1xM Vector for Testing data")

def Generate_matrix():
    global X
    global random_point
    global Training_data
    global Testing_data
    global matrix_dimensions_row
    global matrix_dimensions_column
    
    Training_data = np.random.random((matrix_dimensions_row,matrix_dimensions_column))
    Testing_data = np.random.random((matrix_dimensions_column))
    
    Training_data = Training_data * 5
    Training_data = Training_data.astype(int)
    
    Testing_data = Testing_data * 5
    Testing_data = Testing_data.astype(int)
     
def Calculate_kNN_Parallel(start_index,terminating_index):
    
    global least_distance
    global class_index
    global matrix_dimensions_column
    
    for i in range(start_index,terminating_index):
        temp = 0
        sqrt_result = 1
        TrainingData_temp = 0
        TestingData_temp = 0
        
        for j in range(matrix_dimensions_column):  # Calculate the dot product
            temp += (Training_data[i][j] * Testing_data[j])
            TrainingData_temp += math.pow(Training_data[i][j],2)
            TestingData_temp += math.pow(Testing_data[j],2)
        
        a = math.sqrt(TrainingData_temp)
           
        b = math.sqrt(TestingData_temp)
       
        sqrt_result = a * b
       
        cos_theta = temp / sqrt_result
        
        if cos_theta > least_distance:
            least_distance = cos_theta
            class_index = i
    
    write_lock.acquire()
    if Final_minimum_distance_and_index["min_dist"] < cos_theta:
        Final_minimum_distance_and_index["min_dist"] = cos_theta
        Final_minimum_distance_and_index["min_index"] = class_index
    write_lock.release()
                
def Thread_function():    
    global num_of_threads
    global matrix_dimensions_row
    thread_handle = []
    
    
    for j in range(0,num_of_threads):
        t = Thread(target = Calculate_kNN_Parallel, args=(int((matrix_dimensions_row/num_of_threads) * j),int((matrix_dimensions_row/num_of_threads) * (j+1))))
        
        thread_handle.append(t)
        
        t.start()
        
    for k in range(0,num_of_threads):
        thread_handle[k].join()
        
        
Take_input()
Generate_matrix()
print("\nCalculating . . .\n")
before = time.time()

Thread_function()

after = time.time()

print("\n\n" + str(least_distance) + " and the point which is closest to it has index : " + str(class_index))

print("And the time taken is : " + str(after-before) + " seconds")

# In[2] :

import threading
import random
import time

class ProduceInteger( threading.Thread ):
   """Thread to produce integers"""

   def __init__( self, threadName, sharedObject ):
      """Initialize thread, set shared object"""

      threading.Thread.__init__( self, name = threadName )
      self.sharedObject = sharedObject

   def run( self ):
      """Produce integers in range 1-10 at random intervals"""

      for i in range( 1, 11 ):
         time.sleep( random.randrange( 4 ) )
         self.sharedObject.setSharedNumber( i )

      print (self.getName(), "finished producing values")
      print ("Terminating", self.getName())


# In[3] :
    
import threading
import random
import time

class VehicleThread( threading.Thread ):
   """Class representing a motor vehicle at an intersection"""

   def __init__( self, threadName, event ):
      """Initializes thread"""

      threading.Thread.__init__( self, name = threadName )

      # ensures that each vehicle waits for a green light
      
      self.threadEvent = event

   def run( self ):
      """Vehicle waits unless/until light is green"""

      # stagger arrival times
      
      time.sleep( random.randrange( 1, 10 ) )

      # prints arrival time of car at intersection
      
      print ("%s arrived at %s") % \
         ( self.getName(), time.ctime( time.time() ) )

      # flag is false until two vehicles are queued
      
      self.threadEvent.wait()

      # displays time that car departs intersection
      
      print ("%s passes through intersection at %s") % \
         ( self.getName(), time.ctime( time.time() ) )

greenLight = threading.Event()
vehicleThreads = []

# creates and starts ten Vehicle threads

for i in range( 1, 11 ):
   vehicleThreads.append( VehicleThread( "Vehicle" + str( i ),
      greenLight ) )

for vehicle in vehicleThreads:
   vehicle.start()

while threading.activeCount() > 1:

   # sets the Event object's flag to false
   
   greenLight.clear()
   print ("RED LIGHT!")
   time.sleep( 3 )

   # sets the Event object's flag to true
   
   print ("GREEN LIGHT!")
   greenLight.set()

# In[4] :

import threading

import random

import time

class SemaphoreThread( threading.Thread ):
   """Class using semaphores"""
   

   availableTables = [ "A", "B", "C", "D", "E" ]

   def __init__( self, threadName, semaphore ):
      """Initialize thread"""

      threading.Thread.__init__( self, name = threadName )
      self.sleepTime = random.randrange( 1, 6 )

      # set the semaphore as a data attribute of the class
      
      self.threadSemaphore = semaphore

   def run( self ):
      """Print message and release semaphore"""

      # acquire the semaphore
      
      self.threadSemaphore.acquire()

      # remove a table from the list
      
      table = SemaphoreThread.availableTables.pop()
      print ("%s entered; seated at table %s.") % \
         ( self.getName(), table ),
      print (SemaphoreThread.availableTables)
      time.sleep( self.sleepTime )   # enjoy a meal
     

      # free a table
      print ("   %s exiting; freeing table %s.") % \
         ( self.getName(), table ),
      SemaphoreThread.availableTables.append( table )
      print (SemaphoreThread.availableTables)

      # release the semaphore after execution finishes
      
      self.threadSemaphore.release()

threads = [] 
# list of threads


# semaphore allows five threads to enter critical section

threadSemaphore = threading.Semaphore(
   len( SemaphoreThread.availableTables ) )

# create ten threads

for i in range( 1, 11 ):
   threads.append( SemaphoreThread( "thread" + str( i ),
      threadSemaphore ) )

# start each thread

for thread in threads:
   thread.start()

# In[5] :

# Menunjukkan beberapa thread yang akan menampilkan nama pada interval yang berbeda.

import threading
import random
import time

class PrintThread(threading.Thread):
	"""Subclass dari threading.Thread"""
	def __init__(self, threadName):
		"""Inisialisasi thread, set sleep time, print data"""

		threading.Thread.__init__(self, name=threadName)
		self.sleepTime = random.randrange(1, 6)
		print ("Name: %s; sleep: %d") % \
			(self.getName(), self.sleepTime)

	#overridden Thread run method
	def run(self):
		"""Slee untuk 1-5 detik"""
		
		print (self.getName(), "going to sleep")
		time.sleep(self.sleepTime)
		print (self.getName(), "done sleeping")

thread1 = PrintThread("thread1")
thread2 = PrintThread("thread2")
thread3 = PrintThread("thread3")
thread4 = PrintThread("thread4")

print ("\nStarting thread")

thread1.start() #menjalankan thread
thread2.start() #menjalankan thread
thread3.start() #menjalankan thread
thread4.start() #menjalankan thread

print ("Thread started\n")

# In[6] :
# Program 4: ConsumeInteger.py
# Class that consumes integers

import threading
import random
import time

class ConsumeInteger( threading.Thread ):
   """Thread to consume integers"""

   def __init__( self, threadName, sharedObject ):
      """Initialize thread, set shared object"""

      threading.Thread.__init__( self, name = threadName )
      self.sharedObject = sharedObject

   def run( self ):
      """Consume 10 values at random time intervals"""

      sum = 0             # total sum of consumed values


      # consume 10 values
      
      for i in range( 10 ):
         time.sleep( random.randrange( 4 ) )
         sum += self.sharedObject.getSharedNumber()

      print ("%s retrieved values totaling: %d") % \
         ( self.getName(), sum )
      print ("Terminating", self.getName())

# In[7] :

# Program 5: UnsynchronizedInteger.py

# Unsynchronized access to an integer

import threading

class UnsynchronizedInteger:
   """Class that provides unsynchronized access an integer"""

   def __init__( self ):
      """Initialize shared number to -1"""

      self.sharedNumber = -1

   def setSharedNumber( self, newNumber ):
      """Set value of integer"""

      print ("%s setting sharedNumber to %d") % \
         ( threading.currentThread().getName(), newNumber )
      self.sharedNumber = newNumber

   def getSharedNumber( self ):
      """Get value of integer"""

      tempNumber = self.sharedNumber
      print ("%s retrieving sharedNumber value %d") % \
         ( threading.currentThread().getName(), tempNumber )

      return tempNumber
    

# In[8] :
    
# program 

# menunjukkan multiple thread mengakses shared object

from UnsynchronizedInteger import UnsynchronizedInteger
from ProduceInteger import ProduceInteger
from ConsumeInteger import ConsumeInteger

# initialize integer and threads

number = UnsynchronizedInteger()
producer = ProduceInteger( "Producer", number )
consumer = ConsumeInteger( "Consumer", number )

print ("Starting threads...\n")

# start threads

producer.start()
consumer.start()

# wait for threads to terminate

producer.join()
consumer.join()

print ("\nAll threads have terminated.")

# In[9]

# Fig. 19.8: SynchronizedInteger.py
# Synchronized access to an integer with condition variable
import threading
class SynchronizedInteger:
	"""Class that provides synchronized access an integer"""
	def __init__( self ):
	   """Set shared number, write flag and condition variable"""
	   self.sharedNumber = -1
	   self.writeable = 1      # the value can be changed
	   self.threadCondition = threading.Condition()
	def setSharedNumber( self, newNumber ):
	   """Set value of integer--blocks until lock acquired"""
	   # block until lock released then acquire lock
	   self.threadCondition.acquire()
	   # while not producer's turn, release lock and block
	   while not self.writeable:
	      self.threadCondition.wait()
	   # (lock has now been re-acquired)
	   print ("%s setting sharedNumber to %d") % \
	      ( threading.currentThread().getName(), newNumber )
	   self.sharedNumber = newNumber
	   self.writeable = 0             # allow consumer to consume
	   self.threadCondition.notify() # wake up a waiting thread
	   self.threadCondition.release() # allow lock to be acquired
	def getSharedNumber( self ):
	   """Get value of integer--blocks until lock acquired"""
	   # block until lock released then acquire lock
	   self.threadCondition.acquire()
	   # while producer's turn, release lock and block
	   while self.writeable:
	      self.threadCondition.wait()
	   # (lock has now been re-acquired)
	   tempNumber = self.sharedNumber
	   print ("%s retrieving sharedNumber value %d") % \
	      ( threading.currentThread().getName(), tempNumber )
	   self.writeable = 1             # allow producer to produce
	   self.threadCondition.notify() # wake up a waiting thread
	   self.threadCondition.release() # allow lock to be acquired
	   return tempNumber

# In[10] :
    
# Fig. 19.8: SynchronizedInteger.py

# Synchronized access to an integer with condition variable

import threading

class SynchronizedInteger:
    
	"""Class that provides synchronized access an integer"""
    
	def __init__( self ):
        
	   """Set shared number, write flag and condition variable"""
       
	   self.sharedNumber = -1
	   self.writeable = 1      # the value can be changed
	   self.threadCondition = threading.Condition()
       
	def setSharedNumber( self, newNumber ):
        
	   """Set value of integer--blocks until lock acquired"""
       
	   # block until lock released then acquire lock
	   self.threadCondition.acquire()
	   # while not producer's turn, release lock and block
	   while not self.writeable:
	      self.threadCondition.wait()
	   # (lock has now been re-acquired)
       
	   print ("%s setting sharedNumber to %d") % \
	      ( threading.currentThread().getName(), newNumber )
	   self.sharedNumber = newNumber
	   self.writeable = 0             # allow consumer to consume
	   self.threadCondition.notify() # wake up a waiting thread
	   self.threadCondition.release() # allow lock to be acquired
       
	def getSharedNumber( self ):
        
	   """Get value of integer--blocks until lock acquired"""
       
	   # block until lock released then acquire lock
       
	   self.threadCondition.acquire()
       
	   # while producer's turn, release lock and block
       
	   while self.writeable:
	      self.threadCondition.wait()
          
	   # (lock has now been re-acquired)
       
	   tempNumber = self.sharedNumber
	   print ("%s retrieving sharedNumber value %d") % \
	      ( threading.currentThread().getName(), tempNumber )
	   self.writeable = 1             # allow producer to produce
	   self.threadCondition.notify() # wake up a waiting thread
	   self.threadCondition.release() # allow lock to be acquired
	   return tempNumber

# In[11]:

# Program 4: ConsumeInteger.py

# Class that consumes integers

import threading

import random

import time

class ConsumeInteger( threading.Thread ):
   """Thread to consume integers"""

   def __init__( self, threadName, sharedObject ):
      """Initialize thread, set shared object"""

      threading.Thread.__init__( self, name = threadName )
      self.sharedObject = sharedObject

   def run( self ):
       
      """Consume 10 values at random time intervals"""

      sum = 0             # total sum of consumed values

      # consume 10 values
      
      for i in range( 10 ):
         time.sleep( random.randrange( 4 ) )
         sum += self.sharedObject.getSharedNumber()

      print ("%s retrieved values totaling: %d") % \
         ( self.getName(), sum )
      print ("Terminating", self.getName())

# In[12] :
    
# Program 3: ProduceInteger.py

# Class that produces integers

import threading

import random

import time

class ProduceInteger( threading.Thread ):
   """Thread to produce integers"""

   def __init__( self, threadName, sharedObject ):
      """Initialize thread, set shared object"""

      threading.Thread.__init__( self, name = threadName )
      self.sharedObject = sharedObject

   def run( self ):
      """Produce integers in range 1-10 at random intervals"""

      for i in range( 1, 11 ):
         time.sleep( random.randrange( 4 ) )
         self.sharedObject.setSharedNumber( i )

      print (self.getName(), "finished producing values")
      print ("Terminating", self.getName())

# In[13] :

# Fig. 19.7: fig19_07.py

# Show multiple threads modifying shared object.

from SynchronizedInteger import SynchronizedInteger

from ProduceInteger import ProduceInteger

from ConsumeInteger import ConsumeInteger

# initialize number and threads

number = SynchronizedInteger()
producer = ProduceInteger( "Producer", number )
consumer = ConsumeInteger( "Consumer", number )

print ("Starting threads...\n")

# start threads

producer.start()
consumer.start()

# wait for threads to terminate

producer.join()
consumer.join()

print ("\nAll threads have terminated.")



# In[14]:

from threading import Thread
import math
import numpy as np
import time
import threading

Training_data = []
Testing_data = []

least_distance = 0
class_index = None

matrix_dimensions_row = None
matrix_dimensions_column = None

cosine_similarity_index = 0
num_of_threads = 0

Final_minimum_distance_and_index = {"min_dist":0,"min_index":0}

write_lock = threading.Lock()

def Take_input():
    global matrix_dimensions_row
    global matrix_dimensions_column
    global num_of_threads
    
    matrix_dimensions_row = int(input("Masukkan nomor baris N : "))
    matrix_dimensions_column = int(input("Masukkan nomor kolom M : "))
    num_of_threads = int(input("Masukkan nomor Threads ke : "))
    print("Generating a 1xM Vector for Testing data")

def Generate_matrix():
    global X
    global random_point
    global Training_data
    global Testing_data
    global matrix_dimensions_row
    global matrix_dimensions_column
    
    Training_data = np.random.random((matrix_dimensions_row,matrix_dimensions_column))
    Testing_data = np.random.random((matrix_dimensions_column))
    
    Training_data = Training_data * 5
    Training_data = Training_data.astype(int)
    
    Testing_data = Testing_data * 5
    Testing_data = Testing_data.astype(int)
     
def Calculate_kNN_Parallel(start_index,terminating_index):
    
    global least_distance
    global class_index
    global matrix_dimensions_column
    
    for i in range(start_index,terminating_index):
        temp = 0
        sqrt_result = 1
        TrainingData_temp = 0
        TestingData_temp = 0
        
        for j in range(matrix_dimensions_column):  # Calculate the dot product
            temp += (Training_data[i][j] * Testing_data[j])
            TrainingData_temp += math.pow(Training_data[i][j],2)
            TestingData_temp += math.pow(Testing_data[j],2)
        
        a = math.sqrt(TrainingData_temp)
           
        b = math.sqrt(TestingData_temp)
       
        sqrt_result = a * b
       
        cos_theta = temp / sqrt_result
        
        if cos_theta > least_distance:
            least_distance = cos_theta
            class_index = i
    
    write_lock.acquire()
    if Final_minimum_distance_and_index["min_dist"] < cos_theta:
        Final_minimum_distance_and_index["min_dist"] = cos_theta
        Final_minimum_distance_and_index["min_index"] = class_index
    write_lock.release()
                
def Thread_function():    
    global num_of_threads
    global matrix_dimensions_row
    thread_handle = []
    
    
    for j in range(0,num_of_threads):
        t = Thread(target = Calculate_kNN_Parallel, args=(int((matrix_dimensions_row/num_of_threads) * j),int((matrix_dimensions_row/num_of_threads) * (j+1))))
        
        thread_handle.append(t)
        
        t.start()
        
    for k in range(0,num_of_threads):
        thread_handle[k].join()
        
        
Take_input()
Generate_matrix()
print("\nCalculating . . .\n")
before = time.time()

Thread_function()

after = time.time()

print("\n\n" + str(least_distance) + " and the point which is closest to it has index : " + str(class_index))

print("And the time taken is : " + str(after-before) + " seconds")

# In[2] :

import threading
import random
import time

class ProduceInteger( threading.Thread ):
   """Thread to produce integers"""

   def __init__( self, threadName, sharedObject ):
      """Initialize thread, set shared object"""

      threading.Thread.__init__( self, name = threadName )
      self.sharedObject = sharedObject

   def run( self ):
      """Produce integers in range 1-10 at random intervals"""

      for i in range( 1, 11 ):
         time.sleep( random.randrange( 4 ) )
         self.sharedObject.setSharedNumber( i )

      print (self.getName(), "finished producing values")
      print ("Terminating", self.getName())


# In[3] :
    
import threading
import random
import time

class VehicleThread( threading.Thread ):
   """Class representing a motor vehicle at an intersection"""

   def __init__( self, threadName, event ):
      """Initializes thread"""

      threading.Thread.__init__( self, name = threadName )

      # ensures that each vehicle waits for a green light
      
      self.threadEvent = event

   def run( self ):
      """Vehicle waits unless/until light is green"""

      # stagger arrival times
      
      time.sleep( random.randrange( 1, 10 ) )

      # prints arrival time of car at intersection
      
      print ("%s arrived at %s") % \
         ( self.getName(), time.ctime( time.time() ) )

      # flag is false until two vehicles are queued
      
      self.threadEvent.wait()

      # displays time that car departs intersection
      
      print ("%s passes through intersection at %s") % \
         ( self.getName(), time.ctime( time.time() ) )

greenLight = threading.Event()
vehicleThreads = []

# creates and starts ten Vehicle threads

for i in range( 1, 11 ):
   vehicleThreads.append( VehicleThread( "Vehicle" + str( i ),
      greenLight ) )

for vehicle in vehicleThreads:
   vehicle.start()

while threading.activeCount() > 1:

   # sets the Event object's flag to false
   
   greenLight.clear()
   print ("RED LIGHT!")
   time.sleep( 3 )

   # sets the Event object's flag to true
   
   print ("GREEN LIGHT!")
   greenLight.set()

# In[4] :

import threading

import random

import time

class SemaphoreThread( threading.Thread ):
   """Class using semaphores"""
   

   availableTables = [ "A", "B", "C", "D", "E" ]

   def __init__( self, threadName, semaphore ):
      """Initialize thread"""

      threading.Thread.__init__( self, name = threadName )
      self.sleepTime = random.randrange( 1, 6 )

      # set the semaphore as a data attribute of the class
      
      self.threadSemaphore = semaphore

   def run( self ):
      """Print message and release semaphore"""

      # acquire the semaphore
      
      self.threadSemaphore.acquire()

      # remove a table from the list
      
      table = SemaphoreThread.availableTables.pop()
      print ("%s entered; seated at table %s.") % \
         ( self.getName(), table ),
      print (SemaphoreThread.availableTables)
      time.sleep( self.sleepTime )   # enjoy a meal
     

      # free a table
      print ("   %s exiting; freeing table %s.") % \
         ( self.getName(), table ),
      SemaphoreThread.availableTables.append( table )
      print (SemaphoreThread.availableTables)

      # release the semaphore after execution finishes
      
      self.threadSemaphore.release()

threads = [] 
# list of threads


# semaphore allows five threads to enter critical section

threadSemaphore = threading.Semaphore(
   len( SemaphoreThread.availableTables ) )

# create ten threads

for i in range( 1, 11 ):
   threads.append( SemaphoreThread( "thread" + str( i ),
      threadSemaphore ) )

# start each thread

for thread in threads:
   thread.start()

# In[5] :

# Menunjukkan beberapa thread yang akan menampilkan nama pada interval yang berbeda.

import threading
import random
import time

class PrintThread(threading.Thread):
	"""Subclass dari threading.Thread"""
	def __init__(self, threadName):
		"""Inisialisasi thread, set sleep time, print data"""

		threading.Thread.__init__(self, name=threadName)
		self.sleepTime = random.randrange(1, 6)
		print ("Name: %s; sleep: %d") % \
			(self.getName(), self.sleepTime)

	#overridden Thread run method
	def run(self):
		"""Slee untuk 1-5 detik"""
		
		print (self.getName(), "going to sleep")
		time.sleep(self.sleepTime)
		print (self.getName(), "done sleeping")

thread1 = PrintThread("thread1")
thread2 = PrintThread("thread2")
thread3 = PrintThread("thread3")
thread4 = PrintThread("thread4")

print ("\nStarting thread")

thread1.start() #menjalankan thread
thread2.start() #menjalankan thread
thread3.start() #menjalankan thread
thread4.start() #menjalankan thread

print ("Thread started\n")

# In[6] :
# Program 4: ConsumeInteger.py
# Class that consumes integers

import threading
import random
import time

class ConsumeInteger( threading.Thread ):
   """Thread to consume integers"""

   def __init__( self, threadName, sharedObject ):
      """Initialize thread, set shared object"""

      threading.Thread.__init__( self, name = threadName )
      self.sharedObject = sharedObject

   def run( self ):
      """Consume 10 values at random time intervals"""

      sum = 0             # total sum of consumed values


      # consume 10 values
      
      for i in range( 10 ):
         time.sleep( random.randrange( 4 ) )
         sum += self.sharedObject.getSharedNumber()

      print ("%s retrieved values totaling: %d") % \
         ( self.getName(), sum )
      print ("Terminating", self.getName())

# In[7] :

# Program 5: UnsynchronizedInteger.py

# Unsynchronized access to an integer

import threading

class UnsynchronizedInteger:
   """Class that provides unsynchronized access an integer"""

   def __init__( self ):
      """Initialize shared number to -1"""

      self.sharedNumber = -1

   def setSharedNumber( self, newNumber ):
      """Set value of integer"""

      print ("%s setting sharedNumber to %d") % \
         ( threading.currentThread().getName(), newNumber )
      self.sharedNumber = newNumber

   def getSharedNumber( self ):
      """Get value of integer"""

      tempNumber = self.sharedNumber
      print ("%s retrieving sharedNumber value %d") % \
         ( threading.currentThread().getName(), tempNumber )

      return tempNumber
    

# In[8] :
    
# program 

# menunjukkan multiple thread mengakses shared object

from UnsynchronizedInteger import UnsynchronizedInteger
from ProduceInteger import ProduceInteger
from ConsumeInteger import ConsumeInteger

# initialize integer and threads

number = UnsynchronizedInteger()
producer = ProduceInteger( "Producer", number )
consumer = ConsumeInteger( "Consumer", number )

print ("Starting threads...\n")

# start threads

producer.start()
consumer.start()

# wait for threads to terminate

producer.join()
consumer.join()

print ("\nAll threads have terminated.")

# In[9]

# Fig. 19.8: SynchronizedInteger.py
# Synchronized access to an integer with condition variable
import threading
class SynchronizedInteger:
	"""Class that provides synchronized access an integer"""
	def __init__( self ):
	   """Set shared number, write flag and condition variable"""
	   self.sharedNumber = -1
	   self.writeable = 1      # the value can be changed
	   self.threadCondition = threading.Condition()
	def setSharedNumber( self, newNumber ):
	   """Set value of integer--blocks until lock acquired"""
	   # block until lock released then acquire lock
	   self.threadCondition.acquire()
	   # while not producer's turn, release lock and block
	   while not self.writeable:
	      self.threadCondition.wait()
	   # (lock has now been re-acquired)
	   print ("%s setting sharedNumber to %d") % \
	      ( threading.currentThread().getName(), newNumber )
	   self.sharedNumber = newNumber
	   self.writeable = 0             # allow consumer to consume
	   self.threadCondition.notify() # wake up a waiting thread
	   self.threadCondition.release() # allow lock to be acquired
	def getSharedNumber( self ):
	   """Get value of integer--blocks until lock acquired"""
	   # block until lock released then acquire lock
	   self.threadCondition.acquire()
	   # while producer's turn, release lock and block
	   while self.writeable:
	      self.threadCondition.wait()
	   # (lock has now been re-acquired)
	   tempNumber = self.sharedNumber
	   print ("%s retrieving sharedNumber value %d") % \
	      ( threading.currentThread().getName(), tempNumber )
	   self.writeable = 1             # allow producer to produce
	   self.threadCondition.notify() # wake up a waiting thread
	   self.threadCondition.release() # allow lock to be acquired
	   return tempNumber


   
    