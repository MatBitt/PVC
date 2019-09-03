import cv2
import numpy as np
import time

def pinta(matriz_dist, image, modo):
    if(modo == cv2.IMREAD_GRAYSCALE):
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    B, G, R = cv2.split(image)
    matriz_dist = matriz_dist.astype(np.uint8)
    cv2.bitwise_or(R, matriz_dist, R)
    cv2.bitwise_not(matriz_dist,matriz_dist)
    cv2.bitwise_and(B, matriz_dist, B)
    cv2.bitwise_and(G, matriz_dist, G)
    return cv2.merge((B,G,R))

def criar_matriz_dist(pixel,img, modo):
    if(modo == 1):
        img_aux = np.zeros((img.shape[0],img.shape[1],img.shape[2]))
        img_aux[:] = pixel
        img_aux = img_aux - img
        b, g, r = cv2.split(img_aux)
        dist = np.zeros((img.shape[0],img.shape[1]))
        dist = (b**2 + g**2 + r**2)
        cv2.threshold(dist,(13**2)-1,255,cv2.THRESH_BINARY_INV,dist)
        return dist
    elif(modo == 0):
        dist = np.zeros((img.shape[0],img.shape[1]))
        dist[:] = pixel
        dist = abs(dist - img)
        cv2.threshold(dist,(12),255,cv2.THRESH_BINARY_INV,dist)
        return dist

def mouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Coordinates of pixel: X: ",x,"Y: ",y)
        if modo == 1:
            colorsB = image[y,x,0]
            colorsG = image[y,x,1]
            colorsR = image[y,x,2]
            pixel = image[y,x]
            print("Blue: ",colorsB)
            print("Green: ",colorsG)
            print("Red: ",colorsR)
            print("BGR Format: ",pixel)
            start = time.time()
            distance = criar_matriz_dist(pixel, image, modo)
            result = pinta(distance, image, modo)
            end = time.time()
            cv2.namedWindow('Painted')
            cv2.imshow('Painted',result)

        else:
            print("Intesity :", image[y][x])
            pixel = image[y][x]
            start = time.time()
            distance = criar_matriz_dist(pixel, image, modo)
            result = pinta(distance, image, modo)
            end = time.time()
            cv2.namedWindow('Painted')
            cv2.imshow('Painted',result)

modo = int(input("grayscale :0 colored: 1\n Qual modo você quer? "))

# Read an image, a window and bind the function to window
image = cv2.imread("../Imagens/ntw.jpg", modo)
cv2.namedWindow('Original')
cv2.setMouseCallback('Original',mouse)

#Do until esc pressed
while(1):
    cv2.imshow('Original',image)
    if cv2.waitKey(20) & 0xFF == 27:
        break
#if esc pressed, finish.
cv2.destroyAllWindows()
