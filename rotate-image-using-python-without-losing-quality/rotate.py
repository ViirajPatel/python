#install opencv if you haven't install using py -m pip install opencv
import cv2
# import os utilities
import os
# rotatecodes
#just for fun
# ROTATE_90_CLOCKWISE , ROTATE_90_COUNTERCLOCKWISE , ROTATE_180
for image in os.listdir(os.getcwd()):
    if(image == "rotate.py" or image=="output"): #here i deducted the name of other files and folders
        continue
    else:
        img = cv2.imread(image)
        # rotate and save the image with the same filename
        rotated_img = cv2.rotate(img, rotateCode=cv2.ROTATE_90_COUNTERCLOCKWISE) 
        cv2.imwrite("output\\"+image, rotated_img)#here output is a folder name so if you haven't created then create it !
       

