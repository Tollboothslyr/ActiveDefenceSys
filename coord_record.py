import cv2
import numpy as np
import colorsys 
from base64 import b16encode
import time
cap = cv2.VideoCapture(0)

def rgb2hex(r,g,b):
    hex = "#{:02x}{:02x}{:02x}".format(r,g,b)
    return hex
yeet =1
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        ix, iy = x,y
        
        print(x,y)
        print(event, flags, param)
        ret, img = cap.read()
        dab = img[x,y]
        b = abs(int(dab[0])-255);g = abs(int(dab[1])-255);r = abs(int(dab[2])-255)
        rgb = (b,g,r)
        hsv = colorsys.rgb_to_hsv(r, g, b)
        print(b,g,r)
        print(hsv)
        print(rgb2hex(r,g,b))
        global yeet
        yeet = cv2.circle(img,(x,y), 63, (b,g,r), -1)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    
    ret, img = cap.read()
    cv2.imshow('image',img)
    cv2.imshow('image',yeet)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()