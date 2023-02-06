import cv2 as cv
import numpy as np

imagen = cv.imread('Tareas/Tarea03/Lenna/Lenna.png')
gris=cv.cvtColor(imagen,cv.COLOR_BGR2GRAY)
#umbral=85
#
umbral,binario=cv.threshold(gris,0,255,cv.THRESH_OTSU)

binario=np.uint8((gris<umbral)*255)
cv.imshow('Bianrio',binario)
cv.waitKey(0)