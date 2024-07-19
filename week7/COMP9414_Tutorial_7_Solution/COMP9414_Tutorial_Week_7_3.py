# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 13:51:04 2023

@author: MaryamHashemi
"""
############################### 4.1 Exercise #####################################

############################ 4.1.1 ####################################
import cv2

#captures all the frames
video = cv2.VideoCapture('tom_and_jerry.mp4')

#Check if video opened successfully
if (video.isOpened()== False): 
    print("Error opening video stream or file")

#fram/sec in video and duration of it
fps = video.get(cv2.CAP_PROP_FPS)
print('frames per second =',fps)

#total number of frames
length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
print('total number of frames =',length)
print('duration of the video (in sec) =',length/fps)

video.set(cv2.CAP_PROP_POS_FRAMES, 1002)
ret, frame = video.read()
cv2.imshow('Frame 1002', frame)

cv2.waitKey(0)
cv2.destroyAllWindows()


############################ 4.1.2 ####################################
 
# Read until video is completed
while(video.isOpened()):
  # Capture frame-by-frame
  ret, frame = video.read()
  if ret == True:
    # Display the resulting frame
    cv2.imshow('Original video',frame)

    # framegray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #100 and 200 are lower and upper threshold
    framegray=cv2.Canny(frame,100,200)
    cv2.imshow('Filtered video',framegray)

    if cv2.waitKey(1) == 27:         # wait for ESC key to exit, 27 is the escape key number
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
video.release()
 
# Closes all the frames
cv2.destroyAllWindows()

