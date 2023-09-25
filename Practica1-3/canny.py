# importacion de las librerias
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2


# 1. Suavizar la imagen para eliminar el ruido
def cargarFoto(foto,umbral_superior,umbral_inferior):
     # se carga la imagen
     imag = cv2.imread(foto,0)   # se lee la imagen en BGR
     filas, columnas = imag.shape

     matImg = np.array(imag)

     gauss = np.array([[2, 4, 5, 4, 2],
                    [4, 9, 12, 9, 4],
                    [5, 12, 15, 12, 5],
                    [4, 9, 12, 9, 4],
                    [2, 4, 5, 4, 2]])
     
     sobelX = np.array([[-1,0,1],
                   [-2,0,2],
                   [-1,0,1]])


     sobelY = np.array([[1,2,1],
                    [0,0,0],
                    [-1,-2,-1]])

     matGauss = convolucion(matImg, gauss, filas, columnas)
     matGauss = cv2.normalize(matGauss, None, 0, 255, cv2.NORM_MINMAX) 
     matGauss = np.float64(matGauss)
     matSobelX = convolucion(matGauss, sobelX, filas, columnas)
     matSobelY = convolucion(matGauss, sobelY, filas, columnas)

     matGm = magnitudGradiente(matSobelX,matSobelY)
     matGd = magnitudGradiente(matSobelX,matSobelY)

     matNSM = NoSupresionMazima(matGm,matGd, filas, columnas)
     # Visualizar los bordes detectados
     matHisteresis = UmbralizacionHisteresis(matNSM, filas, columnas,umbral_superior, umbral_inferior)

     imgHisteresis = Image.fromarray(matHisteresis)
     
     return matHisteresis

     
# se realiza el proceso de convolucion
def convolucion(matriz_imagen, kernel, filas, columnas):
     convolucion = np.zeros((filas, columnas))

     for x in range(filas):
          for y in range(columnas):
               for x2 in range(len(kernel)):
                    for y2 in range(len(kernel[0])):
                         if(len(kernel[0]) == 5):
                              if(x>2 and x<filas-2 and y>2 and y<columnas-2):
                                   convolucion[x,y] += (kernel[x2,y2] * matriz_imagen[x-2+x2,y-2+y2])
                         if(len(kernel[0]) == 3):     
                              if(x>1 and x<filas-1 and y>1 and y<columnas-1):
                                   convolucion[x,y] += (kernel[x2,y2] * matriz_imagen[x-1+x2,y-1+y2])
     return convolucion


def magnitudGradiente(derivadaX, derivadaY):
    gm = (derivadaX ** 2 + derivadaY ** 2) ** 0.5
    return gm

def direccionGradiente(derivadaX, derivadaY):
    gd = np.rad2deg(np.arctan2(derivadaY, derivadaX))
    return gd


# Paso 3. No supresion maxima
def NoSupresionMazima(Gm, Gd, filas, columnas):
    Gd_bins = 45 * (np.round(Gd / 45))

    NSM = np.zeros((filas, columnas))

    for r in range(1, filas - 1):
        for c in range(1, columnas - 1):
            angulo = Gd_bins[r, c]

            vecino_a, vecino_b = 0., 0.

            if angulo == 0.:
                vecino_a, vecino_b = Gm[r, c - 1], Gm[r, c + 1]
            elif angulo == 45.:
                vecino_a, vecino_b = Gm[r - 1, c - 1], Gm[r + 1, c + 1]
            elif angulo == 90.:
                vecino_a, vecino_b = Gm[r - 1, c], Gm[r + 1, c]
            elif angulo == 135.:
                vecino_a, vecino_b = Gm[r - 1, c + 1], Gm[r + 1, c - 1]

            if Gm[r, c] >= vecino_a and Gm[r, c] >= vecino_b:
                NSM[r, c] = Gm[r, c]

    return NSM


# Paso 4. Umbralizacion con histeresis
def UmbralizacionHisteresis(HSM, filas, columnas,umbral_inferior, umbral_superior):
    
     # mbrales inferior y superior
     #umbral_inferior = 100
     #umbral_superior = 150

     # Crear una matriz de ceros del mismo tamaño que la imagen
     histeresis = np.zeros((filas,columnas))

     # Aplicar umbralización con histéresis
     for i in range(filas):
          for j in range(columnas):
               if HSM[i, j] > umbral_superior:
                    histeresis[i, j] = 255  # borde Fuerte
               elif HSM[i, j] > umbral_inferior:
                    for x in range(-1, 2):
                         for y in range(-1, 2):
                              if HSM[i + x, j + y] > umbral_superior:
                                   histeresis[i, j] = 255  # borde debil
                              break

     return histeresis


#imagenCanny = cargarFoto('119.jpg',50,100)
#cv2.imshow('Imagen con Canny',imagenCanny)


#imag = Image.open('/119.jpg')   # se lee la imagen en BGR
#filas, columnas = imag.shape

