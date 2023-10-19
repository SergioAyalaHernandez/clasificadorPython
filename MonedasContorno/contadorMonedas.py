import cv2
import numpy as np

original = cv2.imread('monedas3.jpg')
grises = cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)

# Modelado de Gauus
valorGauss = 5
valorKernel = 3
gauss = cv2.GaussianBlur(grises,(valorGauss,valorGauss),0)

kernel=np.ones((valorKernel,valorKernel),np.uint8)

# eliminador de ruidos modelo Canny
canny = cv2.Canny(gauss,60,100)

# para quitar ruido interno o externo, ver la documentación
cierre = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)


contorno, jerarquia = cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(original,contorno,-1,(251,63,52),3)

print("modenas encontrdas: {}".format(len(contorno)))
print("contexto encontrdo: {}".format(len(jerarquia)))

cv2.imshow('Monedas',original)
cv2.imshow('Grises',grises)
cv2.imshow('Gaus',gauss)
cv2.imshow('canny',canny)
cv2.imshow('cierre',cierre)

# le damos un espere
cv2.waitKey(0)

# destruir todas las ventanas abiertas
cv2.destroyAllWindows()