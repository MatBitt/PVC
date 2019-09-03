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
        global clicou
        global pixel_atual
        clicou = True
        pixel_atual = img[y][x]
        if(modo == 1):
            print("linha: ",str(x), " coluna: ", str(y), " B: ",str(img[y][x][0])," G: ",str(img[y][x][1]),"R: ",str(img[y][x][2]))
        else:
            print("linha: ",str(x), " coluna: ", str(y), "Gray: ",str(img[y][x]))
        pass

modo = int(input("grayscale :0 colored: 1\n Qual modo você quer? "))

# Read an image, a window and bind the function to window
video = cv2.VideoCapture('../Vídeos/lee.avi')

valida, img = video.read()
if (not (valida)):
    exit("Error while reading the video, try again.")

cv2.namedWindow('Original')
cv2.setMouseCallback('Original',mouse)
clicou = False

while True:
    flag, img = video.read()
    if flag:
        if(modo == cv2.IMREAD_GRAYSCALE):
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Original', img)
        pos_frame = video.get(cv2.CAP_PROP_POS_FRAMES)
        if(clicou):
            distance = criar_matriz_dist(pixel_atual, img, modo)
            result = pinta(distance, img, modo)
            cv2.namedWindow('Painted')
            cv2.imshow('Painted', result)
    else:
        video.set(cv2.CAP_PROP_POS_FRAMES, pos_frame-1)
        print("frame is not ready")
        cv2.waitKey(10)
    if video.get(cv2.CAP_PROP_POS_FRAMES) == video.get(cv2.CAP_PROP_FRAME_COUNT):
        video.release()
        cv2.destroyWindow('Painted')
        cv2.destroyWindow('Original')
        break
    if cv2.waitKey(25) == 27:
        video.release()
        cv2.destroyWindow('Painted')
        cv2.destroyWindow('Original')
        break
