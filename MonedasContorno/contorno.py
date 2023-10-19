import cv2
import numpy
print(cv2.__version__)

# cargamos imagenes
imagen=cv2.imread('img.jpg')

# copiar y crear en grises
grises = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

_,umbral = cv2.threshold(grises, 150,255, cv2.THRESH_BINARY)
contorno, jerarquia = cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

cv2.drawContours(imagen,contorno,-1,(251,63,52),3)

# mostrar

# cargamos un pantallazo de lo que cargamos en la imagen
cv2.imshow('imagen',imagen)
cv2.imshow('GRISES',grises)
cv2.imshow('umbnral',umbral)

# le damos un espere
cv2.waitKey(0)

# destruir todas las ventanas abiertas
cv2.destroyAllWindows()