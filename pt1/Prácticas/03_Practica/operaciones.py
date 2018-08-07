#Programa 2: Operaciones aritmeticas con imagenes
import cv2
import numpy as np
np.ones=()

#Leyendo la imagen
image = cv2.imread('opencv_logo.png')
image2 = cv2.imread('persona.jpg')
#Crea una matriz de 1 de tipo entero in el mismo tamaño de la imagen
#Entonces lo multiplica por un escalar de 75
#Esto da una matriz co la misma dimensio de nuestra imagen con todos los valores de 75

matrix = np.ones(image.shape, dtype = "uint8") * 255

# Se usa matrix para añadir la matriz a la imagen
#added = cv2.add(image, matrix)
added = cv2.add(image, image2)
cv2.imshow("Sumado", added)

# De la misma forma sucede con la resta
#subtracted = cv2.add(image, matrix)
subtracted = cv2.subtract(image, image2)
cv2.imshow("Restado", subtracted)

#Espera y termina
cv2.waitKey(0)
cv2.destroyAllWindows()
