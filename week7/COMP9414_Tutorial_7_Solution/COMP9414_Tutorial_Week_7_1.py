# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 13:51:04 2023

@author: MaryamHashemi
"""

import numpy as np
import cv2

############################### 3.1 Exercise #####################################

############################ 3.1.1 and 3.1.2 ####################################

#Reading RGB image
img1 = cv2.imread('parrots.jpg')

cv2.imshow('Original image',img1)
print(img1)
print(img1.shape)

img1_red=img1.copy()
img1_red[:,:,2]=255
cv2.imshow('Original image in red',img1_red)


#Reading grey-scale image
img2 = cv2.imread('parrots.jpg',0)
cv2.imshow('Gray-scale image',img2)
print(img2)
print(img2.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()

    

############################ 3.1.3 ####################################

cv2.imwrite('parrots_gray_test.jpg',img2)


############################ 3.1.4 ####################################

#img1 = cv2.imread('parrots.jpg')

height=img1.shape[0]
width=img1.shape[1]
print(height,width)

test=img1.copy()

#Making frame
test[:75,:]=255
test[:,:75]=255
test[height-75:,:]=255
test[:,width-75:]=255

cv2.imshow('Frame test',test)
cv2.imwrite('parrots_frame_test.jpg',test)

cv2.waitKey(0)
cv2.destroyAllWindows()


############################ 3.1.5 ####################################

noise=np.random.random((height,width))
noise=noise*50
noise=noise.astype(int)
print(noise)

cv2.imwrite('noise.jpg',noise)
noise=cv2.imread('noise.jpg',0)
cv2.imshow('Noise',noise)

cv2.waitKey(0)
cv2.destroyAllWindows()


############################ 3.1.6 ####################################

noiseimg=noise + img2
result=cv2.imshow('Image noisy',noiseimg)
cv2.imwrite('parrots_noisy_test.jpg', noiseimg)

cv2.waitKey(0)
cv2.destroyAllWindows()    









