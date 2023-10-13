import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math

def umbralizacionOtsu(imagen):

    imagen = cv2.imread(imagen, 0)   # lee la imagen en escala de grises
    # calcular el histograma
    histograma = np.zeros(256)
    filas, columnas = imagen.shape
    # Realiza el histograma de la imagen
    for x in range(filas):
        for y in range(columnas):
            intensidad = imagen[x, y]
            histograma[intensidad] += 1

    # normalizar el histograma
    histograma = histograma / (filas * columnas)
  
    aux = 0
    final = 0

    # encontrar el umbral optimo
    for umbral in range(1, 256):
        # Calcular w1, w2
        w1 = np.sum(histograma[:umbral])    # suma de 0 al umbral
        w2 = np.sum(histograma[umbral:])    # suma del umbral al final

        if w1 == 0 or w2 == 0:
            continue

        # Calcular x1, x2
        x1 = np.sum(np.arange(umbral) * histograma[:umbral]) / w1
        x2 = np.sum(np.arange(umbral, 256) * histograma[umbral:]) / w2

        #Calcular varianza entre clases
        varianza = w1 * w2 * ((x1 - x2) ** 2)

        if varianza > aux:
            aux = varianza
            final = umbral

    # Paso 5: Aplicar el umbral óptimo
    imagen_binaria = (imagen > final) * 255

    return final,imagen_binaria        



