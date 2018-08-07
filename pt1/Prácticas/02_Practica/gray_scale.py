
#Importante que el formato sea png y/o la imagen no mayor a 1000 pixeles 
import cv2
image = cv2.imread('fruit_2.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.png',gray_image)
cv2.imshow('color_image',image)
cv2.imshow('gray_image',gray_image) 
cv2.waitKey(0)                 # Espera una tecla
cv2.destroyAllWindows()        # Cierra la ventana
 
#End of Code
