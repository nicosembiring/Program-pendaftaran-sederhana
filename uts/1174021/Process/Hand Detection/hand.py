# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:06:30 2020

@author: FAHMI-PC
"""


import cv2
from multiprocessing import Pool

cap = cv2.VideoCapture(0)
hand_cascade = cv2.CascadeClassifier('hand.xml')

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, 1.1, 5)
    
    for(x,y,w,h) in hands:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        
    cv2.imshow('Frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
p = Pool(10)
p.terminate()
p.join()
