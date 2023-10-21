#~*~*~*~*~*~*~*~*~*----------------------BIBLIOTECAS--------------------------*~*~*~*~*~*~*~*~*~*~*~*


from PIL import Image, ImageFilter
from numpy import array
import numpy as np
import matplotlib.pyplot as plt

#~*~*~*~*~*~*~*~*~*----------------------FUNCIONES--------------------------*~*~*~*~*~*~*~*~*~*~*~*


#EROSION

def erosion(array_U,kernel):
    
    dim = np.shape(array_U)
    erosion = np.zeros_like(array_U)
    kernel = kernel.astype(array_U.dtype)  
    for x in range(1, dim[0]-1):
        for y in range(1, dim[1]-1):
            if np.all(array_U[x-1:x+2, y-1:y+2] & kernel):
                erosion[x, y] = 255
    return erosion
                
    
#~*~*~*~*~*~*~*~*~*----------------------PRINCIPAL--------------------------*~*~*~*~*~*~*~*~*~*~*~*


#Se suben imagenes
foto=Image.open("pacman.png")
#Se cambian de tamaño
ancho=200
alto=200
foto=foto.resize((ancho, alto))

#~*~*~*~*~*~*~*~*~*----------------------CIERRE Y APERTURA--------------------------*~*~*~*~*~*~*~*~*~*~*~*


#Se hace la matriz
ker=np.array([[255, 255, 255], [255, 255, 255], [255, 255, 255]])
#Dilatacion
gris=foto.convert("L")

#Umbralizacion
for x in range(foto.size[0]):
    for y in range(foto.size[1]):
        #Si es mayor a 200 osea clarito
        if gris.getpixel((x,y))<100:
            #Lo pone negro
            gris.putpixel((x,y),(0))
        else:
            #Lo pone blanco
            gris.putpixel((x,y),(255))
gris.show()

arr_g=np.array(gris)
#Erosion
e=erosion(arr_g, ker)
er=Image.fromarray(e)
er.show()

arr_g=np.array(gris)
#Resta
r=arr_g-e
#Se enseña
final=Image.fromarray(r)
final.show()
