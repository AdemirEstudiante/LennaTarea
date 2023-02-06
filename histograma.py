import cv2 as cv
import matplotlib.pyplot as pl

imagen = cv.imread('Tareas/Tarea03/Lenna/Lenna.png')
canales=cv.split(imagen)

pl.figure()
pl.title('Histograma')
pl.xlabel('Bins')
pl.ylabel('# de pixeles')
pl.xlim((0,256))

colores=('b','g','r')

for canal,color in zip(canales,colores):
    histograma=cv.calcHist([canal],[0],None,[256],[0,256])
    pl.plot(histograma,color=color)

pl.show()
pl.close()
cv.destroyAllWindows()