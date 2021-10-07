#pylint:disable=no-member

import cv2 as cv
import numpy as np
from numpy.lib.index_tricks import AxisConcatenator

img = cv.imread("..\\Resources\\Photos\\park.jpg")
cv.imshow('Park', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    # rotate around center
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

# +: counter clockwise
# -: clockwise
rotated = rotate(img, -45)
cv.imshow('Rotated Clockwise', rotated)

rotated = rotate(img, 90)
cv.imshow('Rotated Counter Clockwise', rotated)

# previous rotation introduced black traingles into the image
#   so these triangles get rotated too
rotated_rotated = rotate(rotated, 45)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
#   - 0: x-axis 
#   - 1: y-axis
#   - -1: both axis
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)