import cv2
import numpy as np

capturaVideo = cv2.VideoCapture(0)

if not capturaVideo.isOpened():
    print("no se encontró ninguna camara")
    exit()

while True:
    tipoCamara,frame = capturaVideo.read()
    grises = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Camara", grises)

    if cv2.waitKey(1) == ord("q"):
        break

capturaVideo.release()
cv2.destroyAllWindows()