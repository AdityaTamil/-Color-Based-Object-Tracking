import cv2
from PIL import Image
from util import get_limits

COLORS = {
    "yellow":  [0, 255, 255],
    "green":   [0, 255, 0],
    "orange":  [0, 165, 255],
    "pink":    [203, 192, 255],
    "purple":  [128, 0, 128],
}


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    color = COLORS["green"]

    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color)

    mask = cv2.inRange(hsv_img, lowerLimit, upperLimit)
    mask = Image.fromarray(mask)

    bbox = mask.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox 
        frame = cv2.rectangle(frame, (x1,y1), (x2, y2),[0,255,0],3)

    cv2.imshow('webcam_vid', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()