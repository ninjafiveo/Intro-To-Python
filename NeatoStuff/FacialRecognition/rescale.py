import cv2 as cv

img = cv.imread('NeatoStuff/Media/Photos/chocodoggo.jpg')
img2 = cv.imread('NeatoStuff/Media/Photos/chocodoggo.jpg')
cv.imshow('Doggo', img)


def rescaleFrame(frame,  scale=0.10):
    # This works for Images, Videos & Live Video 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #only works for live video - external camera or webcam - will not work on existing  video. 
    capture.set(3, width)
    capture.set(4, height)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

cv.waitKey(0) #0 = keyboard will wait infinitely for something to be pressed. 1000 will wait 1 second. 




#Reading Videos
capture =  cv.VideoCapture('NeatoStuff/Media/Videos/004 Hello World.mp4') # 0 1 2 3 is for attached cameras to pc.

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
            break

capture.release()
cv.destroyAllWindows()
    