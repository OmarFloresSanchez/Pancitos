#~~~~~'_'~'_'~/////+*+*+*+*////-------------BIBLIOTECAS------------\\\*+*+*+\\\\\'_'~'_'~~~~~~


import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math
import random

#~~~~~'_'~'_'~/////+*+*+*+*////-------------FUNCION------------\\\*+*+*+\\\\\'_'~'_'~~~~~~


def conecta(foto):
  #Se lee la imagen y se redimenciona
  foto=cv2.imread(foto,0)
  tamaño=100
  foto=cv2.resize(foto,(tamaño,tamaño))
  #Umbralizacion
  ret,bn = cv2.threshold(foto,50,255,cv2.THRESH_BINARY_INV)
  #Arreglo de la imagen y uno nuevo
  arr_bn=np.asarray(bn)
  arr=np.zeros((tamaño, tamaño))
  #Iteraciones
  num=0
  paro=0
  while(paro==0):
    arr2=arr
    for i in range(tamaño):
      for j in range(tamaño):
        if(arr_bn[i,j]==255):
          if(i>1 and i<tamaño-1 and j>1 and j<tamaño-1):
            if(arr[i,j-1]==0 and arr[i,j+1]==0 and arr[i-1,j]==0 and arr[i+1,j]==0):
              num+=1
              arr[i,j]=num
            elif(arr[i,j-1]!=0 or arr[i,j+1]!=0 or arr[i-1,j]!=0 or arr[i+1,j]!=0):
                prov=[arr[i,j-1], arr[i,j+1], arr[i-1,j], arr[i+1,j]]
                #print(prov)
                minimus=min(prov)
                #print(minimus)
                if(minimus==0):
                    b=[]
                    for k in range(len(prov)):
                        if(prov[k]!=0):
                            b.append(prov[k])
                    #print(b)
                    arr[i,j]=min(b)
                else:
                    arr[i,j]=minimus
        elif(arr_bn[i,j]==0):
          arr[i,j]=(0)
    if(arr2.all()==arr.all()):
      paro=1
      break
  
  
  #Arreglos de 3 canales
  arr_r=np.zeros((tamaño, tamaño))
  arr_g=np.zeros((tamaño, tamaño))
  arr_b=np.zeros((tamaño, tamaño))
  #Coloreacion de las rayitas
  for blanco in range(1000):
    ran_r=random.randint(0,255)
    ran_g=random.randint(0,255)
    ran_b=random.randint(0,255)
    for i in range(tamaño):
      for j in range(tamaño):
        if(arr[i,j]==blanco and blanco!=0):
          arr_r[i,j]=ran_r
          arr_g[i,j]=ran_g
          arr_b[i,j]=ran_b
  #Union en nueva imagen
  union=np.zeros((tamaño, tamaño,3), dtype=np.uint8)
  union[:,:,0] = arr_r  
  union[:,:,1] = arr_g  
  union[:,:,2] = arr_b  
  imagen = Image.fromarray(union)
  nyb=Image.fromarray(arr_bn)
  #Imagen final
  imagen.show()
  nyb.show()
  
 #~~~~~'_'~'_'~/////+*+*+*+*////-------------PRINCIPAL------------\\\*+*+*+\\\\\'_'~'_'~~~~~~  
  
      
conecta("7.JPG")
