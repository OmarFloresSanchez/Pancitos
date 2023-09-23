#~~~~~'_'~'_'~/////+*+*+*+*////-------------BIBLIOTECAS------------\\\*+*+*+\\\\\'_'~'_'~~~~~~


import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#~~~~~'_'~'_'~/////+*+*+*+*////-------------LECTURA DE LA IMAGEN-------------\\\*+*+*+\\\\\'_'~'_'~~~~~~


#Se lee la imagen.
foto=cv2.imread('Amici.jpg')

#~~~~~'_'~'_'~/////+*+*+*+*////-------------COSAS UTILES-------------\\\*+*+*+\\\\\'_'~'_'~~~~~~


tamaño=200
#SE REDIMENCIONA.

foto=cv2.resize(foto,(600,450))
#SE PASA A GRISES.

gris=cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
#SUAVISADO GAUSIANO.

gaus= cv2.GaussianBlur(gris,(5,5),0)
#EROCION Y DILATACION.

kernel = np.ones((5,5),np.uint8)
#GRADIENTE.

gradiente = cv2.morphologyEx(gaus, cv2.MORPH_GRADIENT, kernel)
#APERTURA.

apertura = cv2.morphologyEx(gradiente, cv2.MORPH_CLOSE, kernel)
#DILATACION.

#dilatasion = cv2.dilate(apertura,kernel,iterations = 1)
#UMBRALIZACION.

ret,thresh= cv2.threshold(apertura,100,255,cv2.THRESH_BINARY)
#Se enseña.
cv2.imshow('Pokemon XY', thresh)

