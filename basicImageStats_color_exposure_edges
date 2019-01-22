#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Adriana Stohn
Jan 21 2019

Retrieve: 
    average color of an image, 
    average exposure/brightness of an image ( luminance channel), 
    number of edges for a given pixel value threshold (decision boundary of derivative)
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


#Read Image
img = cv2.imread('/Users/adrianastohn/Desktop/CRCHistoPhenotypes_2016_04_28/Detection/img1/img1.bmp')
#Display Image
plt.imshow(img)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


#Find average value of each color channel (RGB)
redAvg = img[:,:,0].mean()
greenAvg = img[:,:,1].mean()
blueAvg = img[:,:,2].mean()

#Display each color channel
plt.imshow(img[:,:,0],cmap='gray')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

plt.imshow(img[:,:,1],cmap='gray')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

plt.imshow(img[:,:,2],cmap='gray')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


"""
In RGB images, image "brightness" is calculated as luminance. The weights in the 
luminance calculation are correlated to the photopic response of the eye, or how 
strongly the human eye perceives each color.
Luminance = (0.2126*R + 0.7152*G + 0.0722*B)
"""
#Luminance Calculation
lumMat = 0.2126*img[:,:,0] + 0.7152*img[:,:,1] + 0.0722*img[:,:,2]
plt.imshow(lumMat,cmap='gray')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

lumAvg = 0.2126*redAvg + 0.7152*greenAvg + 0.0722*blueAvg



"""
The three most common types of edge detection algorithms are: Sobel, Laplacian, 
and Canny edge detections. Sobel detection relies on the first derivative, 
Laplacian relies on the second derivative, and Canny edge detection is by 
intensity gradient.

"""

edges = cv2.Canny(img,10,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()




"""
The Blob detection that is NOT WORKING
"""

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()
 
# Change thresholds
params.minThreshold = 10;
params.maxThreshold = 200;
 
# Filter by Area.
params.filterByArea = False
params.minArea = 1500
 
# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.1
 
# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.87
 
# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.01
 
# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else : 
    detector = cv2.SimpleBlobDetector_create(params)

#detector = cv2.SimpleBlobDetector()
#
#imgGray = lumMat.astype(int)    
#
#keypoints = detector.detect(imgGray)
#im_with_keypoints = cv2.drawKeypoints(imgGray, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#cv2.imshow("Keypoints",im_with_keypoints)







