import cv2 as cv

img = cv.imread('E:\OpenCV\photos\Battlefield 1 Screenshot 2021.07.22 - 19.37.40.47.png')

cv.imshow('Main', img)

#Untuk bikin contours harus bikin gambarnya gray dan temukan titik pinggir/edges
#ATAU bikin TRESHOULD

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)

#Menemukan titik pinggir/Edges menggunakan canny
# canny = cv.Canny(img, 127,175)
# cv.imshow('Canny', canny)

#Canny Blur
canny = cv.Canny(blur, 127,175)
cv.imshow('Canny', canny)

#Menemukan contours tanpa di blur dahulu akan
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(f'ada sebanyak {len(contours)} contours dengan menggunakan metode NONE ')

#Hasil dari temuan contours tetap sama walaupun beda metode dikarenakan kebanyakan edges/titik pinggir dalam images
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f'ada sebanyak {len(contours)} contours dengan menggunakan metode SIMPLE ')

#Apa yang terjadi ketika gambarnya di blur sebelum menemukan titik pinggir images
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f'ada sebanyak {len(contours)} contours dengan menggunakan metode SIMPLE dan di Blur')


cv.waitKey(0)
