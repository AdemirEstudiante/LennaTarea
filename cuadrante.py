import cv2 as cv

imagen = cv.imread('Tareas/Tarea03/Lenna/Lenna.png')

shear=imagen[0:256,0:256]

cv.imshow('Cuadrante',shear)
cv.waitKey(0)