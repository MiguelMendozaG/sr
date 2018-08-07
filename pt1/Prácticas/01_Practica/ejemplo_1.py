
#Programa 1: Concepto basico, cargar mostrar y dividir colores de una imagen
import cv2 as cv
 
img = cv.imread('logos.png')
b,r,g = cv.split(img)
img2 = cv.merge((b,g,r))
cv.imshow('Image', img)
cv.imshow('Image2', img2) 
cv.waitKey(0)
cv.destroyAllWindows()
	
cv.imwrite('newlogos.png',img2)
