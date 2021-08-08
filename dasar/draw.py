import cv2 as cv
import numpy as np

# img = cv.imread('E:\OpenCV\photos\Battlefield 1 Screenshot 2021.07.22 - 21.38.00.17.png')
# cv.imshow('Images',img)

blank = np.zeros((500,500,3), dtype='uint8') #untuk nanti kalau mau warna 
#500 = Height/Tinggi, 500 = Width/Lebar, 3=Warna

#untuk mengubah warna bisa seperti ini
# blank[:] = 52, 152, 219 #warna kuning tua memakai RGB

# #untuk ngasih warna di gambar pada lokasi tertentu
# #bisa memakai seperti ini

# blank[200:300,200:300] = 52, 152, 219

# cv.imshow('Kuning Tua',blank)

# # Gambar persegi panjang
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(52, 152, 219),thickness=cv.FILLED) #cv.FILLED untuk warnain kotanya atau bisa make -1
# #(0,0) Lokasi original, (250,250) Destinasi lokasi, Warna memakai RGB, thickness border
# cv.imshow('Kotak',blank)

# #Gambar Bulat
# cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2),40,(52, 152, 219),thickness=3)
# cv.imshow('Circle',blank)

# #Gambar garis
# cv.line(blank, (0,0),(blank.shape[1]//2,blank.shape[0]//2),(52, 152, 219),thickness=3)
# cv.imshow('Garis',blank)


# #TEXT di dalam GAMBAR
# cv.putText(blank, 'HELLO', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (52, 152, 219), 2)
# cv.imshow('TEXT',blank)

cv.waitKey(0)
