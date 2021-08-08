import cv2 as cv

#Reading Images
img = cv.imread('photos/Battlefield 1 Screenshot 2021.07.22 - 19.37.40.47.png')

cv.imshow('BattleField', img)

#Reading Video

# capture = cv.VideoCapture('videos/Watch Dogs 2 2021.06.03 - 16.38.52.01.mp4') #bisa make angka 0,1,2,3 kalau terkonek ke webcam 
# #contoh 0 webcam 1 webcam 2 dll

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Videos',frame)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

# cv.waitKey(0)