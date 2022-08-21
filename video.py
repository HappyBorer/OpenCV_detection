import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# img = cv2.imread('OpenCV_detection/faces.jpg')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# faces = face_cascades.detectMultiScale(img_gray)
# for (x, y, h, w) in faces:
#     cv2.rectangle(img, (x, y), (x + h, y + w), (255, 0, 0), 1)
    
# cv2.imshow('Result', img)
# cv2.waitKey(0)

cap = cv2.VideoCapture('OpenCV_detection/video.mp4')

while True:
    success, frame = cap.read()
   
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascades.detectMultiScale(img_gray)
    
    for (x, y, h, w) in faces:
        cv2.rectangle(frame, (x, y), (x + h, y + w), (255, 0, 0), 1)
    
    cv2.imshow('Result', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

