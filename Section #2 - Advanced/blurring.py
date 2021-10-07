#pylint:disable=no-member

import cv2 as cv

# kernel is a window drawn on the image 
# blur is applied to the middle pixel based on the surrounding pixels

img = cv.imread("..\\Resources\\Photos\\cats.jpg")
cv.imshow('Cats', img)

# Averaging
#   - middle pixel intensity will be average of surrounding pixel intensity
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
#   - surrounding pixels are given a weight and then averaged
#   - gives less blur but looks for natural
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
#   - middle pixel intensity will be median of surrounding pixel intensity
#   - more effective at reducing substantial noise
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
#   - applies blurring but retains edges
#   - slow
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)