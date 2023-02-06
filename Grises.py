import cv2 as cv

imagen = cv.imread('Tareas/Tarea03/Lenna/Lenna.png')
gris=cv.cvtColor(imagen,cv.COLOR_BGR2GRAY)

cv.imshow('Escala de grises',gris)
cv.waitKey(0)