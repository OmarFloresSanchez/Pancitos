#~~~~~'_'~'_'~/////+*+*+*+*////-------------BIBLIOTECAS------------\\\*+*+*+\\\\\'_'~'_'~~~~~~


import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math

#~~~~~'_'~'_'~/////+*+*+*+*////-------------LECTURA DE LA IMAGEN-------------\\\*+*+*+\\\\\'_'~'_'~~~~~~


#Se lee la imagen
foto=cv2.imread('On.jpg')

#~~~~~'_'~'_'~/////+*+*+*+*////-------------COSAS UTILES-------------\\\*+*+*+\\\\\'_'~'_'~~~~~~


tamaño=200
#Se redimenciona
foto=cv2.resize(foto,(tamaño,tamaño))

#~~~~~'_'~'_'~/////+*+*+*+*////-------------OPERACIONES-------------\\\*+*+*+\\\\\'_'~'_'~~~~~~


#Cany xd
cany=cv2.Canny(foto,200,200)
#Se enseña
cv2.imshow('Pokemon XY',cany)
#Se quita
cv2.waitKey(1000);
cv2.destroyAllWindows()

#Se pasa a arreglo
arreglo=np.asarray(cany)
#Acomulador
p=276
h=np.zeros((p,180))
acomulador=[]
#Se hacen fors
for i in range(tamaño):
    for j in range(tamaño):
        cont=[]
        ds=[]
        if(arreglo[i,j]==255):
            for angulo in range(180):
                p=i*math.cos(angulo)+j*math.sin(angulo)
                p=int(p)
                h[p,angulo]+=1
                #cont.append(angulo)
                #ds.append(p)
            #plt.plot(cont,ds)
            #plt.show()
maximo=np.max(h)    
print(maximo)
angulo=0
p=0
for i in range(276):
    for j in range(180):
        if(h[i,j]==maximo):
            angulo=j
            p=i
print(angulo)
print(p)
rayas=np.zeros((tamaño, tamaño))
for i in range(tamaño):
    for j in range(tamaño):
        
        operacion=i*math.cos(angulo)+j*math.sin(angulo)-p
        if(operacion<1 and operacion>-1):
            rayas[i, j]=255
            
imagen = Image.fromarray(rayas)
imagen.show()
