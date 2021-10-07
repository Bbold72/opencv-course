#pylint:disable=no-member

import cv2 as cv
import numpy as np

img = cv.imread("..\\Resources\\Photos\\cats.jpg")
cv.imshow('Cats', img)


blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)
blank = img

# 1. Paint the image a certain colour
blank[200:300, 200:300] = 0,0,255
cv.imshow('Red', blank)

# 2. Draw a Rectangle
# thickness=-1 fills in circle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

# 3. Draw A circle
cv.circle(blank, (blank.shape[1]//2+20, blank.shape[0]//2+20), 40, (12,123,255), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Brian!!!', (10,330), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)