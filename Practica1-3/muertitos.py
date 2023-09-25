#~~~~~'_'~'_'~/////+*+*+*+*////-------------BIBLIOTECAS------------\\\*+*+*+\\\\\'_'~'_'~~~~~~


import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math
import canny

#~~~~~'_'~'_'~/////+*+*+*+*////-------------TRANSFORMADA-------------\\\*+*+*+\\\\\'_'~'_'~~~~~~

def hough(foto,umbral):

  #Se lee la imagen
  foto_gris=cv2.imread(foto,cv2.IMREAD_GRAYSCALE)

#~~~~~'_'~'_'~/////+*+*+*+*////-------------OPERACIONES-------------\\\*+*+*+\\\\\'_'~'_'~~~~~~

  #Cany xd
  # iamgen , umbral minimo, umbral maximo
  #cany=cv2.Canny(foto,100,200,apertureSize=3)
  cany = canny.cargarFoto(foto,60,80)
  filas, columnas = cany.shape


  #cv2.imshow('Canny', cany)
  #cv2.waitKey(0)
  #cv2.destroyAllWindows()

  #Se pasa a arreglo
  arreglo=np.asarray(cany)

  res_p = 1
  res_t = np.pi/180 # angulo en radianes
  #Acomulador
  p = int(math.sqrt(filas**2 + columnas**2))  # se hace pitagoras
  theta = 180  # Ángulos de -90 a 90 grados

  acumulador = np.zeros((p, theta), dtype=np.uint64) # para que no haya valores negativos

  # obtiene la matriz de acumulacion
  for x in range(filas):
    for y in range(columnas):
      if(cany[x,y] == 255):  # si se detecta un punto de borde
       for t in range(theta):   # recorre los 180 grados
        r = int(x * math.cos(math.radians(t)) + y * math.sin(math.radians(t))) # para que se utilizen en radianes
        acumulador[r,t] += 1

  print(acumulador)
  
  # se establece un umbral para saber cuales son lineas
  #umbral = 300
  maximos_locales = []

  for r in range(p):
    for t in range(theta):
      if(acumulador[r,t] > umbral):
        maximos_locales.append((r,t)) # lss guarda como coordenadas polare          

  # pintar las lineas
  final = cv2.cvtColor(foto_gris, cv2.COLOR_GRAY2BGR)

  for r, t in maximos_locales:
    # los convierte a coordenadas cartesianas
      a = math.cos(math.radians(t))
      b = math.sin(math.radians(t))
      x0 = a * r
      y0 = b * r
      
      # inicio y fin de la linea
      x1 = int(x0 + 1000 * (-b))
      y1 = int(y0 + 1000 * (a))
      x2 = int(x0 - 1000 * (-b))
      y2 = int(y0 - 1000 * (a))
      cv2.line(final, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Dibuja la línea en la imagen original
   # Muestra la imagen con líneas detectadas
   #cv2.imshow('Imagen con líneas', final)
   #cv2.waitKey(0)
   #cv2.destroyAllWindows()
  return final


# *****************************************************
# --------------- ESPACIO DE HOUGH --------------------
# *****************************************************
def espacioHough(foto,maximos):
    grafico_hough = np.zeros((len(maximos), 360), dtype=np.uint8)

    #lista1 = [x[0] for x in maximos]  # Lista con los valores en la primera posición de cada tupla
    #lista2 = [x[1] for x in maximos]  # Lista con los valores en la segunda posición de cada tupla

    for i in range(len(maximos)):
        p, t = maximos[i]
        p = int(p)
        t = int(np.degrees(t)) % 360
        
        # Incrementar el valor en el espacio de Hough
        grafico_hough[i, t] = 255
    
    return grafico_hough
 

# ****************************************************************
# ----------------- IMPRIME LAS LINEAS Y EL ESPACIO -------------
# ****************************************************************

filas = 1
columnas = 5
axes = []
fig = plt.figure()

for i in range(filas*columnas):
    ruta = "juanmecanico/" + str(i) + ".png"
    print(ruta)
    img = hough(ruta,230)

    axes.append(fig.add_subplot(filas, columnas, i+1))
    subplot_title1=("Imagen "+str(i))
    axes[-1].set_title(subplot_title1)  
    plt.imshow(img)

fig.tight_layout()
plt.show()



