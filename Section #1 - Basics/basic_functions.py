#pylint:disable=no-member

import cv2 as cv

# Read in an image
img = cv.imread("..\\Resources\\Photos\\park.jpg")
cv.imshow('Park', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
#   -  
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# will decrease number of edges found significantly
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges with Blur', canny)

# Dilating the image
# can make edges thicker
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
# removes delation and basically returns canny
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
# interpolation=cv.INTER_AREA: useful for shrinking image
# interpolation=cv.INTER_CUBIC: useful for increasing image
#   - LINEAR is faster but CUBIC gives better quality
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)