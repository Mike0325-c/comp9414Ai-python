# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 13:51:04 2023

@author: MaryamHashemi
"""
############################### 3.2 Exercise #####################################

import cv2
import numpy as np

############################ 3.2.1 ####################################
def mean_filter(image):
    height=image.shape[0]
    width=image.shape[1]
    img=image.copy()
    for i in range(height):
        for j in range(width):
            if  (i>1 and j>1 and i<height-1 and j<width-1): 
                a=image[i-1,j-1]/9
                b=image[i,j-1]/9
                c=image[i-1,j]/9
                d=image[i,j+1]/9
                e=image[i+1,j]/9
                f=image[i+1,j+1]/9
                g=image[i+1,j-1]/9
                h=image[i-1,j+1]/9
                k=image[i,j]/9
                n=a+b+c+d+e+f+g+h+k
    #           print(img1[i-1,j-1],img1[i,j-1])
                img[i,j]=int(n)
                
    return cv2.imshow('Filtered image (mean)',img)

############################ 3.2.2 ####################################
def median_filter(image):
    height=image.shape[0]
    width=image.shape[1]
    img_prime=image.copy()
    for i in range(height):
        for j in range(width):
            if(i>1 and j>1 and i<height-1 and j<width-1):
                a=[image[i,j],image[i+1,j+1],image[i-1,j-1],image[i,j+1],image[i+1,j],image[i-1,j],image[i+1,j-1],image[i-1,j+1],image[i,j-1]]
                img_prime[i,j]=np.median(a)

    return cv2.imshow('filtered image (median)',img_prime)



img1 = cv2.imread('parrots.jpg',0)
cv2.imshow('Gray-scale image',img1)

img2=cv2.imread('parrots_noisy_test.jpg',0)
cv2.imshow('Image noisy',img2)            

mean_filter(img2)
median_filter(img2)


############################ 3.2.3 ####################################
window=3

# Apply the mean filter
ksize = (window, window)  # Size of the filter kernel
opencv_mean_image = cv2.blur(img2, ksize)


# Apply the median filter
ksize = window  # Size of the filter kernel (window size)
opencv_median_image = cv2.medianBlur(img2, ksize)

cv2.imshow('OpenCV filtered image (mean)',opencv_mean_image)
cv2.imshow('OpenCV filtered image (median)',opencv_median_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
