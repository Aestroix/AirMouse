import cv2
import numpy as np
kernel = np.ones((5,5), np.uint8)

'''
img = cv2.imread('1.jpeg') # to read image

cv2.imshow('My', img) # to show image
cv2.waitKey(0)
'''
frameWidth = 500
frameHeight = 800
cap = cv2.VideoCapture(0)  # to take the video input parameter 0 says input device 0 ( camera )

while True:
    success, frame = cap.read() # read frame one by one
    '''
        after reading the frame one by one you can perform as many operations as you want
    '''
    frame = cv2.resize(frame, (frameWidth, frameHeight)) # resizing
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # grayscaling it
    # cv2.imshow('me', frame)
    # frame = cv2.Canny(frame, 50, 150)  # find the borders around images in the frame
    cv2.rectangle(frame, (20, 20), (480, 780),(0,0,255), 2) # draws line/ rectangle/ circle
    cv2.imshow('me1', frame) # outputs the frame
    # frameDilation = cv2.dilate(frame, kernel, iterations = 1)
    # cv2.imshow('me1', frameDilation)

    if cv2.waitKey(1) & 0xFF == ord('q'): # waitkey is the waiting period in milliseconds
        # here 0xFF statement is checking the input of q key and it terminates the output
        break



