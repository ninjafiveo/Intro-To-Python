import cv2 as cv
import numpy as np

# Create a blank image
blank = np.zeros((500, 500, 3), dtype = 'uint8') #3 = number of color channels
cv.imshow('Blank', blank)

# img = cv.imread('NeatoStuff/Media/Photos/twodogs.jpg')
# cv.imshow('Doggo', img)

# blank[:] = 0,255,0
# blank[:] = 255,0,0
# blank[:] = 0,0,255
# blank[:] = 255,255,255
# blank[:] = 0,255,255
#1. Paint an image in the box.
blank[100:300, 200:300] = 0,255,255 #100:300 = Height of square, 200:300 width of inner square
cv.imshow('Green', blank)

#2. Draw a rectangle
# cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness=5) #Outline
# cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness=cv.FILLED) #(Filled Box)
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[1]//2), (0, 255, 0), thickness=cv.FILLED) #(Filled Box)
cv.imshow('Rectangle', blank)

#3. Draw a circle
cv.circle(blank, (400,400), 40, (255,0,0), thickness=3)
cv.imshow('Circle', blank)

#4. Line
cv.line(blank, (100,0),  (400,400), (200,100, 200), thickness=3)
cv.imshow('Line', blank)

#5. Write Text
cv.putText(blank, 'What up Ninja?', (100, 200), cv.FONT_HERSHEY_COMPLEX, 1.0, (50,55,155), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)

# Left off at 31:59
# https://www.youtube.com/watch?v=oXlwWbU8l2o&t=26s
