import cv2

cap = cv2.VideoCapture('OpenCV_detection/video.mp4')

while True:
    success, frame = cap.read()
    cv2.imshow('result', frame)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

