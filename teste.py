import cv2
import numpy as np
import sys
import numpy as np
import cv2
from threading import Thread

hsf_select = 0;
min_value = 100;
max_value = 255;
select = True;
troquei = False;

class Regular(Thread):
    """docstring for regular."""
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        while (1):
            hsf_select = raw_input("digita hsf: \n")
            min_value = raw_input("digita min: \n")
            max_value = raw_input("digita max: \n")
            troquei = True;



blue = float(sys.argv[1])/255.0
green = float(sys.argv[2])/255.0
red = float(sys.argv[3])/255.0

color = np.float32([[[blue, green, red]]])
hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

hue = hsv_color[0][0][0]
hsf_select = 5;


cap = cv2.VideoCapture(0)


seletor = Regular(1)

jogafora = True
while(1):

    if select:
        seletor.start()
        select = False
    if troquei:
        print (hsf_select + " , " + min_value + " , " + max_value)
        troquei = False
    # Take each frame

    # _, frame = cap.read()
    frame  = cv2.imread('soja4.jpeg')

    if jogafora:
        jogafora = False
    else:
        # jogafora = True

        #ponto flutuante
        #h ,w, b = frame.shape

        hsv = (frame/255.0).astype(np.float32)
        print hsv[0][0][0]
        # Convert BGR to HSV
        #hsv = np.zeros(frame.shape)
        hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)

        print hsv[0][0][0]

        # define range of blue color in HSV
        lower_blue = np.array([hue-hsf_select,0,0])
        upper_blue = np.array([hue+hsf_select,1,1])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame,frame, mask= mask)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

cv2.destroyAllWindows()
