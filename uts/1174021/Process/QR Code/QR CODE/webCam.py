# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:05:11 2020

@author: FAHMI-PC
"""

#import library

import cv2

import multiprocessing as mp

import threading
import queue
from time import sleep

try:
    NUMB_PROCESSES = mp.cpu_count()
    
except NotImplementedError:
    
    NUMB_PROCESSES = 1
NUMB_THREADS_PER_PROCESS = 8
Q = mp.Queue()

#--------------------------------------------------------------------\
#--------------------------------------------------------------------\


#pastikan semua telah terinstall
#terutama opencv

#--------------------------------------------------------------------\
#--------------------------------------------------------------------\


def show_webcam(mirror=False):
    
    cam = cv2.VideoCapture(0)
    while True:
        
        ret_val, img = cam.read()
        if mirror:
            img = cv2.flip(img, 1)
        cv2.imshow('Leitor', img)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()




#--------------------------------------------------------------------\
    
    
def main():
    show_webcam(mirror=True)
    
    

#--------------------------------------------------------------------\
    
    
if __name__ == '__main__':
    main()
    
    
#--------------------------------------------------------------------\
#--------------------------------------------------------------------\
    
# menguji lewat processing dan threading

class CustomThread(threading.Thread):
    """This functions the same as the inherited Thread
    class except with added semaphore parameter, which
    always releases the semaphore when the thread is done.
    """
    
    def __init__(self, semaphore=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._semaphore = semaphore

    def run(self):
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            if self._semaphore:
                self._semaphore.release()
            del self._target, self._args, self._kwargs



def do_work(i, process_name):
    """Do the heavy processing."""
    sleep(0.5)
    print('Process Number: {}, value: {}'.format(
        process_name,i*i))



def populate_queue():
    """Fill up the queue with work to do.
    Additional work will not be added."""
    for x in range(10000):
        Q.put(x)



def run_threads(p_name, semaphore):
    """As long as there are items on the queue,
    i.e. work to do, then we keep threading."""
    while not Q.empty():
        semaphore.acquire()
        try:
            i = Q.get(timeout=1)
        except queue.Empty:
            break
        CustomThread(
            target=do_work, daemon=1,
            args=(i,p_name), semaphore=semaphore
        ).start()



def start_processes():
    
    """Initialize the queue 
    with work and start
    a number of process 
    (defined above). With
    each process, we create 
    a bounded semaphore
    to control the number 
    of active threads
    per process."""
    
    populate_queue()
    
    process_list = []
    
    for x in range(NUMB_PROCESSES):
        semaphore = threading.BoundedSemaphore(
            NUMB_THREADS_PER_PROCESS)
        
        # pass the semaphore to the target func
        p = mp.Process(
            target=run_threads,
            args=(x,semaphore,), name=str(x)
        )
        process_list.append(p)
        
        p.start()
        
    for process in process_list:
        # make sure all processes have completed
        
        process.join()
##
##
##
#fungsi main

if __name__ == '__main__':
    start_processes()
