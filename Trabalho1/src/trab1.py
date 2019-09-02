import cv2
import numpy as np

def mouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        print("Coordinates of pixel: X: ",x,"Y: ",y)
        if modo == 1:
            colorsB = image[y,x,0]
            colorsG = image[y,x,1]
            colorsR = image[y,x,2]
            colors = image[y,x]
            print("Blue: ",colorsB)
            print("Green: ",colorsG)
            print("Red: ",colorsR)
            print("BGR Format: ",colors)

        else:
            print("Intesity :", image[y][x])

modo = int(input("grayscale :0 colored: 1\n Qual modo você quer? "))

# Read an image, a window and bind the function to window
image = cv2.imread("../Imagens/ntw.jpg", modo)
cv2.namedWindow('mouse')
cv2.setMouseCallback('mouse',mouse)

#Do until esc pressed
while(1):
    cv2.imshow('mouse',image)
    if cv2.waitKey(20) & 0xFF == 27:
        break
#if esc pressed, finish.
cv2.destroyAllWindows()
