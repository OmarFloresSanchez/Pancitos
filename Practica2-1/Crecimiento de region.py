#~~~~~'_'~'_'~/////+*+*+*+*////-------------BIBLIOTECAS------------\\\*+*+*+\\\\\'_'~'_'~~~~~~


import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math

#~~~~~'_'~'_'~/////+*+*+*+*////-------------LECTURA DE LA IMAGEN-------------\\\*+*+*+\\\\\'_'~'_'~~~~~~


#Se lee la imagen
foto=cv2.imread('mri.jpg')
#foto=cv2.imread('On.jpg')

#~~~~~'_'~'_'~/////+*+*+*+*////-------------COSAS UTILES-------------\\\*+*+*+\\\\\'_'~'_'~~~~~~


tamaño=200
#Se redimenciona
foto=cv2.resize(foto,(tamaño,tamaño))
#Se enseña
#cv2.imshow('Pokemon XY',foto)
#Coordenadas xy
x=68
y=92
foto[x,y]=3,3,255
#Se marca el puntito
cv2.imshow('Cambiada',foto)

#~~~~~'_'~'_'~/////+*+*+*+*////-------------OPERACIONES-------------\\\*+*+*+\\\\\'_'~'_'~~~~~~


#Escala de grises
gris=cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
gris[x,y]=255
cv2.imshow('Gris xd',gris)
#Matriz
mat_gris=np.asarray(gris)
# R
r=78
#Umbral
u=30
#Recorrido
tamañin=tamaño-1
for i in range(tamaño):
    for j in range(tamaño):
        if(i<tamañin and j<tamañin and i>0 and j>0):
            if(foto[i,j]==3,3,255):
                #Guarda las coordenadas
                dif=abs(gris[i-1,j-1]-r)
                if(dif<=u):
                    foto[i-1,j-1]=3,3,255
                        
                dif=abs(gris[i-1,j+1]-r)
                if(dif<=u):
                    foto[i-1,j+1]=3,3,255
                        
                dif=abs(gris[i+1,j-1]-r)
                if(dif<=u):
                    foto[i+1,j-1]=3,3,255
                        
                dif=abs(gris[i+1,j+1]-r)
                if(dif<=u):
                    foto[i+1,j+1]=3,3,255
                        
                dif=abs(gris[i+1,j]-r)
                if(dif<=u):
                    foto[i+1,j]=3,3,255
                        
                dif=abs(gris[i,j+1]-r)
                if(dif<=u):
                    foto[i,j+1]=3,3,255
                        
                dif=abs(gris[i-1,j]-r)
                if(dif<=u):
                    foto[i-1,j]=3,3,255
                        
                dif=abs(gris[i,j-1]-r)
                if(dif<=u):
                    foto[i,j-1]=3,3,255
                
cv2.imshow('Gris xd',gris)
cv2.imshow('Foto final',foto)
        
