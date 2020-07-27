# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:05:11 2020

@author: FAHMI-PC
"""


#--------------------------------------------------------------------\
#--------------------------------------------------------------------\
#Import library

from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse

import multiprocessing as mp

import imutils
import time
import cv2

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


# 

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="output.csv",)  
#

args = vars(ap.parse_args())
#--------------------------------------------------------------------\
#--------------------------------------------------------------------\
# 


print("[INFO] Output in a file output.csv")
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
csv = open(args["output"], "w")
found = set()

#--------------------------------------------------------------------\
#--------------------------------------------------------------------\
# 


while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    barcodes = pyzbar.decode(frame)

    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text = "{}".format(barcodeData)
        cv2.putText(frame, '', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        if barcodeData not in found:

            csv.write("{}\n".format(barcodeData))
            csv.flush()

            found.clear()
            found.add(barcodeData)

    cv2.imshow("Scan QR code <test>", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break
    
#--------------------------------------------------------------------\
#--------------------------------------------------------------------\
#
        
    
print("[INFO] Output in a file output.csv")
csv.close()
cv2.destroyAllWindows()
vs.stop()

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
