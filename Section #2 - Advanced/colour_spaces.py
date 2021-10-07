#pylint:disable=no-member

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("..\\Resources\\Photos\\park.jpg")
cv.imshow('Park', img)

# opencv reads images as BGR instead of RBG
plt.imshow(img)
plt.show()

# BGR to Grayscale
#   - grayscale images basically show you the distribution of color intensity
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV - Hue Saturation Value
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

cv.waitKey(0)