# Tutorial https://www.youtube.com/watch?v=oXlwWbU8l2o&t=26s

import cv2 as cv

# img = cv.imread('NeatoStuff/Media/Photos/chocodoggo.jpg')
# cv.imshow('Doggo', img)
# cv.waitKey(0) #0 = keyboard will wait infinitely for something to be pressed. 1000 will wait 1 second. 

#Reading Videos
capture =  cv.VideoCapture('NeatoStuff/Media/Videos/004 Hello World.mp4') # 0 1 2 3 is for attached cameras to pc.


#use while loop to read frame by frame
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()