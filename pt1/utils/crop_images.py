import cv2
import numpy as np
import glob
import os
 
cropping = False
 
x_start, y_start, x_end, y_end = 0, 0, 0, 0
count_img = 0

input_folder = "/home/miguelmg/Documents/Smart_Robotics/dataset/cerdo/cerdo"
if not os.path.exists(input_folder + "/crop"):
    os.makedirs(input_folder + "/crop")

input_folder_crop = input_folder + "/crop"
dir_images = glob.glob(input_folder + "/*.jpg")

def mouse_crop(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping, count_img
 
    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True
 
    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y
 
    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        cropping = False # cropping is finished
 
        refPoint = [(x_start, y_start), (x_end, y_end)]
 
        if len(refPoint) == 2: #when two points were found
            roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            cv2.imwrite(input_folder_crop + "/" + str(count_img) + "_crop.jpg",roi)
            count_img = count_img + 1
            cv2.imshow("Cropped", roi)

for dir_image in dir_images:
    image = cv2.imread(dir_image)
    oriImage = image.copy()
    #print (dir_image)
    #cv2.imshow("image" + dir_image, image )
     
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", mouse_crop)

    true = 1
    while true:

        i = image.copy()

        if not cropping:
            cv2.imshow("image", image)
            croped = 0

        elif cropping:
            cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
            cv2.imshow("image", i)
            croped = 1

        if cv2.waitKey(1) & 0xFF == ord('c'):
            true = 0

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
# close all open windows
cv2.destroyAllWindows()
