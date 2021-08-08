import cv2 as cv
import numpy as np

img2 = cv.imread('E:\OpenCV\photos\Battlefield 1 Screenshot 2021.07.22 - 21.38.00.17.png')

cv.imshow('Contoh',img2)

# #Translation/Geser gambar/Geser Video
# def translate(img, x, y):
#     transMat = np.float32([[1,0,x],[0,1,y]])
#     dimension = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transMat, dimension)

# # -x gambar/video akan geser ke kiri
# # -y gambar/video akan geser ke atas
# # x gambar/video akan geser ke kanan
# # y gambar/video akan geser ke bawah

# translated = translate(img2, 2, 2)
# cv.imshow('translated',translated)


# #Rotasi
# def rotate(img, angle, rotPoint=None):
#     (width,height) = img.shape[:2]

#     if rotPoint is None:
#         rotPoint = (width//2,height//2)

#     rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
#     dimension = (width,height)
#     return cv.warpAffine(img, rotMat, dimension)

# rotasi = rotate(img2,45)
# cv.imshow('Rotasi',rotasi)


#Resizing
# resized = cv.resize(img2, (500,500), interpolation=cv.INTER_LINEAR)
# cv.imshow('Resize', resized)


# #Flip
# flip = cv.flip(img2, -1)#Flip Code ada 3 yaitu 0, 1, dan -1
# cv.imshow('Flip',flip)

#Cropping
crop = img2[200:200, 300:400]
cv.imshow('crop',crop)

cv.waitKey(0)