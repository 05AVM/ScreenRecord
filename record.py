#making a screen recorder using Python..
import cv2 # opencv ka module cv2 The cv2 module is the main module in OpenCV that provides developers with an easy-to-use interface for working with image and video processing functions.

import pyautogui
from win32api import GetSystemMetrics # to wrok with screen resoltuions..
import numpy as np
import time # to campture the time we require to shoot the video..

width=GetSystemMetrics(0)
height=GetSystemMetrics(1)
# It captures the full screen resoltuions..

dim=(width,height)
f=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter("test.mp4",f,30.0,dim) # we can change the location also..but in that case we need to  give the full path..
# then we pass the video format..the frames persecond and the dimension of the video..
start_time=time.time()
dur=10
end_time=start_time+dur
while True: 
    #becuase we need capture the photo so we run a loop..
    image=pyautogui.screenshot()
    #we are taking a screenshot of the image..and the making an array  out of it..
    frame=np.array(image)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #to save the original color..
    output.write(frame)
    if time.time()>end_time : #if the current time is greater
        break               #than the end time..then break from the loop..
output.release()                   #releasing the memory occupied by the video file..
print("---END---")
