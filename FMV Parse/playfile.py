import numpy as np
import cv2

print cv2.__version__

cap = cv2.VideoCapture('att.MP4')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    green = np.uint8([[[0, 255, 0]]])

    # Our operations on the frame come here
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgbhsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    #hsv_green = cv2.cvtColor(frame, hsv)

    # Display the resulting frame
    cv2.imshow('BGRHSV', hsv)
    cv2.imshow('GRAY', gray)
    cv2.imshow('RGBHSV', rgbhsv)
    cv2.imshow('mask', mask)
    #cv2.imshow('hsv_green', hsv_green)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()