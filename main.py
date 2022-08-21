import cv2

img = cv2.imread('OpenCV_detection/image.jpg')
 
#print(img.shape)
  
#print(img)
img = cv2.resize(img, (500, 500))

cv2.imshow('Result', img)

cv2.waitKey(0)
