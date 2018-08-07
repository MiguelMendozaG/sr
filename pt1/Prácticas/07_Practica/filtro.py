#Filtro Gaussiano
import cv2
import numpy as np

img = cv2.imread('golden_bridge.jpg')
rows, cols = img.shape[:2]

#Generando una mascara vignette usando Gauss
kernel_x = cv2.getGaussianKernel(cols,200)
kernel_y = cv2.getGaussianKernel(rows,200)
kernel = kernel_y * kernel_x.T
mask = 255 * kernel / np.linalg.norm(kernel)
output = np.copy(img)

#Aplicando la mascara a cada canal en la entrada de la imagen
for i in range(3):
    output[:,:,i] = output[:,:,i] * mask

cv2.imshow('Original', img)
cv2.imshow('Vignette', output)
cv2.waitKey(0)
