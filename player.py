#!/usr/bin/python3

import cv2
import numpy as np

# create a video capture object and read from input file
cap = cv2.VideoCapture('tree.mp4')

# check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video file")

# Read until video is Completed
while (cap.isOpened()):
    # capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q to exit
        if cv2.waitKey(25) & 0xFF == ord('Q'):
            break
    # Break the loop
    else:
        break

# when everythind done, release the video capture object
cap.release()

# closes all the frames
cv2.destroyAllWindows()
