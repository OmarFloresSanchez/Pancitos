# ----- IMPORTACION DE LIBRERIAS -----
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math

# ----- NOMBRE DE LAS IMAGENES DE PRUEBAaaa -----
foto1 = "carretera.jpg"
foto2 = "image-cell.png"
foto3 = "person_bacteria.jpeg"


def umbralizacionGlobal(imagen, umbral):
     filas, columnas = imagen.shape
     imagen = np.array(imagen)     # convierte la imagen a arreglo


     for x in range(filas):
          for y in range(columnas):
               if imagen[x, y] > umbral:
                    imagen[x, y] = 255  # lo pone en blanco
               else:
                    imagen[x, y] = 0    # lo pone en negro
                    
     return imagen

# ----- LLAMADO DE LAS FUNCIONES -----
imagen = cv2.imread(foto3,0)  # lee la imagen en escala de grises

Uglobal = umbralizacionGlobal(imagen,120)    # llama a la funcion con un umbral n

imgGlobal = Image.fromarray(Uglobal)    # pasa el arreglo a imagen

# Muestra la imagen original y la imagen umbralizada
# ---- imagen 1 ------
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(imagen, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(imgGlobal, cmap='gray')
plt.title('Imagen Umbralizada (General)')
plt.axis('off')

plt.show()