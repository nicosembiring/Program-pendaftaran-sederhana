import cv2
import numpy as np





recognizer = cv2.face.LBPHFaceRecognizer_create()




recognizer.read('trainer/trainer.yml')




cascadePath = "Classifiers/face.xml"



faceCascade = cv2.CascadeClassifier(cascadePath);



Id = 0





cam = cv2.VideoCapture(0)





font = cv2.FONT_HERSHEY_SIMPLEX






while True:




    ret, im =cam.read()





    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)




    faces=faceCascade.detectMultiScale(gray, 1.2,5)




    for(x,y,w,h) in faces:


        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)



        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])



        if(conf<50):
            if(Id==1):
                Id="Fahmi"
            elif(Id==2):
                Id="Dzihan"







        else:
            Id="Unknown"
        cv2.putText(im,str(Id), (x,y+h),font,2,(0,255,0), 2)
    cv2.imshow('webcam',im) 
    if cv2.waitKey(10) & 0xFF==ord('x'):
        break







cam.release()
cv2.destroyAllWindows()

# In[2] 
import cv2
import numpy as np
import os
import pickle
import sqlite3
import serial
import time







Myserial = serial.Serial('COM5',9600, timeout = 1)
time.sleep(2)








def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)








def profile(Id):
    conn=sqlite3.connect("FaceRecg.db")
    cmd="SELECT * FROM Data WHERE Id="+str(Id)
    cursor=conn.execute(cmd)
    data=None
    for rows in cursor:
        data=rows
    conn.close()
    return data







# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()





assure_path_exists("trainer/")





# Load the trained mode

recognizer.read('trainer/trainer.yml')







# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"






# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);







# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX








# Initialize and start the video frame capture
cam = cv2.VideoCapture(+1)






# Loop
while True:




    # Read the video frame
    ret, im =cam.read()




    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)




    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)





    # For each face in faces
    for(x,y,w,h) in faces:




        # Create rectangle around the face
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)





        # Recognize the face belongs to which ID
        Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        Name=profile(Id)
        if(Name!=None):
             cv2.putText(im, str(Name[1]) , (x,y-40), font, 1, (255,255,255), 3)
           
    




    # Display the video frame with the bounded rectangle
    cv2.imshow('im',im) 






    if (len(faces)) == 1:
        if(Id == 1):
            Myserial.write(b'Y')
            print ("Face is detected")
    elif (len(faces)) == 0:
        Myserial.write(b'N')
        print ("No face is detected")

 
    
    
    
    
    
    k = cv2.waitKey(1) & 0xFF == ord('q')
    if k == 1:
        break






# Stop the camera
cam.release()







# Close all windows
cv2.destroyAllWindows()