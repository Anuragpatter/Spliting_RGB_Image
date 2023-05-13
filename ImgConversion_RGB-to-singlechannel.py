# Importing cv2 module into Python
import cv2 as cv

# read the image using imread built in function in cv2
image = cv.imread("Path_to_image")

#convert the image to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

#print the image array
print(gray)
print("")

#printing the shape of array in the form (height , width , number of channels)
print(gray.shape)

#convert the image to RGB (images are read in BGR in OpenCV)
RGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)
#print the image array
print(RGB)
print("")

#print the shape of the image array
print(RGB.shape)

#VISUALIZATION OF EACH CHANNEL SEPERATELY

import numpy as np

#convert the image to RGB (images are read in BGR in OpenCV)
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

#split the image into its three channels
(R,G,B) = cv.split(image)

#create named windows for each of the images we are going to display
cv.namedWindow("Blue", cv.WINDOW_NORMAL)
cv.namedWindow("Green", cv.WINDOW_NORMAL)
cv.namedWindow("Red", cv.WINDOW_NORMAL)

#display the images
cv.imshow("Blue",B)
cv.imshow("Green", G)
cv.imshow("Red", R)

#write the images to disk
cv.imwrite("[Disk_name]://[Folder_name]//channel_red.jpg", R)
cv.imwrite("[Disk_name]://[Folder_name]//channel_green.jpg", G)
cv.imwrite("[Disk_name]://[Folder_name]//channel_blue.jpg", B)
if cv.waitKey(0):
    cv.destroyAllWindows()
