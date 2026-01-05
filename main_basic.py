import cv2
#from PIL import Image
from util import get_limits

COLORS = {
    "yellow":  [0, 255, 255],
    "red":     [0, 0, 255],
    "green":   [0, 255, 0],
    "blue":    [255, 0, 0],
    "orange":  [0, 165, 255],
    "pink":    [203, 192, 255],
    "purple":  [128, 0, 128],
    "white":   [255, 255, 255],
    "black":   [0, 0, 0],
    "gray":    [128, 128, 128]
}


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    color = COLORS["purple"]

    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color)

    mask = cv2.inRange(hsv_img, lowerLimit, upperLimit)
    x1, y1, w, h = cv2.boundingRect(mask)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv2.contourArea(cnt) > 800:
            x1, y1, w, h = cv2.boundingRect(cnt)
        
    frame = cv2.rectangle(frame, (x1,y1), (x1 + w, y1 + h),[0,255,0],3)

    cv2.imshow('webcam_vid', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()