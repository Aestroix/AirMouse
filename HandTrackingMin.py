#  BARE MINIMUM CODE REQUIRED FOR HAND TRACKING
from cv2 import *
import mediapipe as mp
import time
#####################
cap = VideoCapture(0) # default camera
frameWidth = 500
frameHeight = 800
while True:
    success, frame = cap.read()
    frame = resize(frame, (frameWidth, frameHeight))
    imshow('Camera', frame)
    waitKey(1)


