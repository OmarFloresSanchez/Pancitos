# ----- IMPORTACION DE LIBRERIAS -----
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math

def umbralizacion_bernsen(foto, kernel, umbral):
    # ----- LLAMADO DE LAS FUNCIONES -----
    imagen = cv2.imread(foto,0)    # lee la imagen en escala de grises
    imagen = np.array(imagen)   # convierte la imagen a arreglo

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
                resultado[x, y] = 0
            else:
                resultado[x, y] = 255

    return resultado



