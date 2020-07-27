import cv2
import numpy as np
import threading





#Import sqlite for Database
import sqlite3






detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Using Classifier for face detecting
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#Using Classifier for eye_detecting
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#VideoCapture













class BuatThread(threading.Thread):
    def insert(Id,Name):
        conn=sqlite3.connect("FaceRecg.db")
        cmd="SELECT * FROM Data WHERE Id="+str(Id)
        cursor=conn.execute(cmd)
        flag=0
        for row in cursor:
            flag=1;
            if(flag==1):
                cmd1="UPDATE Data SET Name=' "+str(Name)+" ' WHERE ID="+str(Id)
                conn.execute(cmd1) 
            else:
                cmd1="INSERT INTO Data(ID,Name) Values("+str(Id)+",' "+str(Name)+" ' )"
                conn.execute(cmd1)   
                conn.commit()
                conn.close()
    








Id=input('Enter Your Id::')#Console Input
name=input('Enter Your Name::')#Console Input
insert(Id,name)





Count=0#Count Value For counting and stroing images









while True:






    # Read the video frame
    ret, im =cam.read()







    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)







    # Get all face from the video frame
    faces = detector.detectMultiScale(gray, 1.3,5)







    # For each face in faces
    for(x,y,w,h) in faces:






        # Create rectangle around the face
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
        roi_gray = gray[y:y+h, x:x+w]#Fetching face from gray 





        #incrementing sample Count 
        Count=Count+1


        #saving the captured face in the dataset folder
        cv2.imwrite("dataset/User."+Id +'.'+ str(Count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('webcam',im)







    #wait for 100 miliseconds 
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break






    # break if the sample Count is morethan 20
    elif Count>20:
        break
    










cam.release()
cv2.destroyAllWindows()






# In[2]
import cv2


cam = cv2.VideoCapture(0)



detector=cv2.CascadeClassifier('Classifiers/face.xml')


i=0


offset=50


name=input('enter your id')



while True:


    ret, im =cam.read()


    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)



    faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)



    for(x,y,w,h) in faces:


        i=i+1


        cv2.imwrite("dataSet/face-"+name +'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])


        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)


        cv2.imshow('im',im[y-offset:y+h+offset,x-offset:x+w+offset])


        cv2.waitKey(100)





    if i>20:
        cam.release()
        cv2.destroyAllWindows()
        break