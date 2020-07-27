import cv2







# Import numpy for matrix calculation
import numpy as np







# Import Python Image Library (PIL)
from PIL import Image







import os







def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)




# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()





# Using prebuilt frontal face training model, for face detection
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");






# Create method to get the images and label data
def getImagesAndLabels(path):




    # Get all file path
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
    



    # Initialize empty face sample
    faceSamples=[]
    






    # Initialize empty id
    ids = []






    # Loop all the file path
    for imagePath in imagePaths:






        # Get the image and convert it to grayscale
        PIL_img = Image.open(imagePath).convert('L')




        # PIL image to numpy array
        img_numpy = np.array(PIL_img,'uint8')





        # Get the image id
        id = int(os.path.split(imagePath)[-1].split(".")[1])





        # Get the face from the training images
        faces = detector.detectMultiScale(img_numpy)






        # Loop for each face, append to their respective ID
        for (x,y,w,h) in faces:




            # Add the image to face samples
            faceSamples.append(img_numpy[y:y+h,x:x+w])






            # Add the ID to IDs
            ids.append(id)






    # Pass the face array and IDs array
    return faceSamples,ids





# Get the faces and IDs
faces,ids = getImagesAndLabels('dataset')






# Train the model using the faces and IDs
recognizer.train(faces, np.array(ids))






# Save the model into trainer.yml
assure_path_exists('trainer/')
recognizer.save('trainer/trainer.yml')

# In[2]

import cv2,os


import numpy as np


from PIL import Image 



recognizer = cv2.face.LBPHFaceRecognizer_create()


cascadePath = "Classifiers/face.xml"


faceCascade = cv2.CascadeClassifier(cascadePath);


path = 'dataSet'




def get_images_and_labels(path):
     image_paths = [os.path.join(path, f) for f in os.listdir(path)]


     # images will contains face images
     images = []


     # labels will contains the label that is assigned to the image
     labels = []
     for image_path in image_paths:


         # Read the image and convert to grayscale
         image_pil = Image.open(image_path).convert('L')


         # Convert the image format into numpy array
         image = np.array(image_pil, 'uint8')


         # Get the label of the image
         nbr = int(os.path.split(image_path)[1].split(".")[0].replace("face-", ""))


         #nbr=int(''.join(str(ord(c)) for c in nbr))
         print (nbr)


         # Detect the face in the image
         faces = faceCascade.detectMultiScale(image)


         # If face is detected, append the face to images and the label to labels
         for (x, y, w, h) in faces:

             images.append(image[y: y + h, x: x + w])

             labels.append(nbr)

             cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])

             cv2.waitKey(10)

     # return the images list and labels list
     return images, labels



images, labels = get_images_and_labels(path)


cv2.imshow('test',images[0])


cv2.waitKey(1)


recognizer.train(images, np.array(labels))


recognizer.write('trainer/trainer.yml')


#recognizer.save('trainer/trainer.yml')
cv2.destroyAllWindows()