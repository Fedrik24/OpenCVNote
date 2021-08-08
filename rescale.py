import cv2 as cv

img = cv.imread('photos/Battlefield 1 Screenshot 2021.07.22 - 21.35.30.17.png')
cv.imshow('images',img)

def rescaleFrame(frame, scale=0.75):
    #Metode ini berguna untuk Images, Video dan Live Video
    width = int(frame.shape[1]  * scale) #untuk lebar makai frame.shape[1]
    height = int(frame.shape[0] * scale) #untuk tinggi makai frame.shape[0]
    dimesion = (width,height)

    return cv.resize(frame,dimesion, interpolation=cv.INTER_AREA)

# def changeRes(width,height):
#     #Metode ini berguna hanya untuk Live Video
#     capture.set(3,width)
#     capture.set(4,height)

resized_image = rescaleFrame(img)
cv.imshow('Images', resized_image)
cv.waitKey(0)


# capture = cv.VideoCapture('videos/Watch Dogs 2 2021.06.03 - 16.38.52.01.mp4') #bisa make angka 0,1,2,3 kalau terkonek ke webcam 
# #contoh 0 webcam 1 webcam 2 dll

# while True:
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame,scale=.2)

#     cv.imshow('Videos',frame)
#     cv.imshow('Videos',frame_resized)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()