# ----- IMPORTACION DE LIBRERIAS -----
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math

def umbralizacion_bernsen(imagen, kernel, umbral):
    filas, columnas = imagen.shape  
    resultado = np.zeros_like(imagen)   # hace una matriz de 0 del tamaño de la imagen

    radio = kernel // 2    # hace una division con un resultado entero para saber el radio del kernel

    for x in range(radio, filas - radio): # se hace la convolucion de la ventana
        for y in range(radio, columnas - radio):
            ventana = imagen[x - radio:x + radio + 1,
                             y - radio:y + radio + 1]
            
            min_pixel = np.min(ventana) # obtiene el minimo pixel 
            max_pixel = np.max(ventana) # obtiene el maximo pixel 

            if max_pixel - min_pixel <= umbral: # si la suma de ellos es menor al umbral...
                resultado[x, y] = 255
            else:
                resultado[x, y] = 0

    return resultado


# ----- NOMBRE DE LAS IMAGENES DE PRUEBA -----
foto1 = "carretera.jpg"
foto2 = "image-cell.png"
foto3 = "person_bacteria.jpeg"


# ----- LLAMADO DE LAS FUNCIONES -----
imagen = cv2.imread(foto3,0)    # lee la imagen en escala de grises
imagen = np.array(imagen)   # convierte la imagen a arreglo

kernel = 15 # Tamaño de la ventana 
umbral = 20  # Umbral minimod de los vecinos
imagen_umbralizada = umbralizacion_bernsen(imagen, kernel, umbral)

# Muestra la imagen original y la imagen umbralizada
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(imagen, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(imagen_umbralizada, cmap='gray')
plt.title('Imagen Umbralizada (Bernsen)')
plt.axis('off')

plt.show()