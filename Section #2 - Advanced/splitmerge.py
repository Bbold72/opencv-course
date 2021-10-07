#pylint:disable=no-member

import cv2 as cv
import numpy as np

# take images and split into three color channels: blue, green and red


img = cv.imread("..\\Resources\\Photos\\park.jpg")
cv.imshow('Park', img)

b, g, r = cv.split(img)

# displays as grayscale image because has shape of one in last axis
# grayscale is distribution of color intensity
#   - white is very intense; black is not
cv.imshow('Blue - Grayscale', b)
cv.imshow('Green - Grayscale', g)
cv.imshow('Red - Grayscale', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# add blank axis to display colors
blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

# reconstruct original image from three color channel images
merged = cv.merge([b, g, r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)