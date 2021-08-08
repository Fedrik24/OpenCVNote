from typing import ChainMap
import cv2 as cv

img = cv.imread('E:\OpenCV\photos\Battlefield 1 Screenshot 2021.07.22 - 21.41.02.79.png')

cv.imshow('Battle', img)

# #Covert to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

#Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blue',blur)

# #Cari Edge
# cany = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', cany)

# #dilating images

# dilated = cv.dilate(cany, (7,7), iterations=1)
# cv.imshow('Dilated',dilated)

# #eroding
# eroed = cv.erode(dilated,(3,3),iterations=1)
# cv.imshow('eroed',eroed)

#Resize/Crop
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resize',resized)

#Crop
cropped = img[50:100,300:400]
cv.imshow('crop',cropped)

cv.waitKey(0)
