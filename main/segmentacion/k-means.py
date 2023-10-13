# ----- IMPORTACION DE LIBRERIAS -----
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math
from ..detectores_formas.canny import cargarFoto
from ..bordes.otsu import umbralizacionOtsu
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D 


# ----- SE APLICA UNA DILATACION -----
def dilatacion(imagen, tam):
    kernel = np.ones((tam, tam), np.uint8)  # Puedes ajustar el tamaño del kernel según tus necesidades

    erosionada = np.zeros_like(imagen)  # Crea una imagen de ceros del mismo tamaño

    for i in range(1, filas):
        for j in range(1, columnas ):
            # Aplica la operación de erosión
            area = imagen[i - 1:i + 1, j - 1:j + 1]
            erosionada[i, j] = np.min(area)  # El valor mínimo en la vecindadsu, np.ones((7, 7), np.uint8))

    cv2.imwrite('dilatacion.png', erosionada)
    plt.imshow(erosionada,cmap='gray')

    return 

# la imagen es la que ta contiene los contornos
def encontrar_contornos():
     contornos, _ = cv2.findcontornos(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

     imgContornos = canny.copy()
     imgContornos = cv2.cvtColor(imgContornos, cv2.COLOR_GRAY2BGR)
     cv2.drawcontornos(imgContornos, contornos, -1, (0, 255, 0), 3)

     finalcontornos = []
     tabla_medias = pd.DataFrame()
     for i, cont in enumerate(contornos):
          area = int(cv2.contArea(cont))

          # if area is higher than 3000:
          if area > 1000:
               finalcontornos.append(cont)
               # get mean color of cont:
               filtro = np.zeros_like(imagen[:, :, 0])  # This mask is used to get the mean color of the specific bead (cont), for kmeans
               cv2.drawcontornos(filtro, [cont], 0, 255, -1)

               mediaB, mediaG, mediaR, _ = cv2.mean(imagen, mask=filtro)
               df = pd.DataFrame({'mediaB': mediaB, 'mediaG': mediaG, 'mediaR': mediaR}, index=[i])
               tabla_medias = pd.concat([tabla_medias, df])


     contornos_img_after_filtering = canny.copy()
     contornos_img_after_filtering = cv2.cvtColor(contornos_img_after_filtering, cv2.COLOR_GRAY2BGR)
     cv2.drawcontornos(contornos_img_after_filtering, tuple(finalcontornos), -1, (0, 255, 0), 3)
     cv2.imwrite('contornos.png', cv2.hconcat([imgContornos, contornos_img_after_filtering]))

     return tabla_medias

# ----- INICIO K-MEANS -----
def distancia(punto1, punto2):
     return np.sqrt(np.sum((punto1 - punto2) ** 2))

def puntosCentroidas(datos, centroides):
     asignaciones = np.zeros(len(datos))
     for i, punto in enumerate(datos):
          distancias = [distancia(punto, centroide) for centroide in centroides]
          asignaciones[i] = np.argmin(distancias)
     return asignaciones

def calcular_nuevos_centroides(datos, asignaciones, K):
     nuevos_centroides = []
     for i in range(K):
          puntos_asignados = datos[asignaciones == i]
          nuevo_centroide = np.mean(puntos_asignados, axis=0)
          nuevos_centroides.append(nuevo_centroide)
     return np.array(nuevos_centroides)

def kmeans(tabla_medias,k):
     # Extrae los valores de mediaB, mediaG y mediaR
     mediaB = tabla_medias['mediaB'].to_numpy()
     mediaG = tabla_medias['mediaG'].to_numpy()
     mediaR = tabla_medias['mediaR'].to_numpy()

     data = np.column_stack((mediaB, mediaG, mediaR))

     # Inicialización  centroides al azar
     centroides = data[np.random.choice(len(data), k, replace=False)]

     tolerancia = 1e-4

     # Iterar hasta que los centroides converjan
     for _ in range(300):  # Límite máximo de iteraciones
          asignaciones = puntosCentroidas(data, centroides)
          nuevos_centroides = calcular_nuevos_centroides(data, asignaciones, k)
     
          # Comprobar la convergencia
          if np.all(np.abs(centroides - nuevos_centroides) < tolerancia):
               break     
     
     centroides = nuevos_centroides

     return centroides, data, asignaciones

# ----- IMAGENES DE PRUEBA -----
foto = 'burbujas.png'
imagen = cv2.imread(foto)
filas, columnas,_ = imagen.shape

# ----- UMBRALIZACION CON OTSU -----
umbral,imgOtsu = umbralizacionOtsu(foto)

dilatacion(imgOtsu,2)

# ----- DETECCION DE BORDES CON CANNY -----
canny = cargarFoto('dilatacion.png', umbral, umbral-10)
imgCanny = Image.fromarray(canny)
cv2.imwrite('canny.png', canny)

canny = canny.astype(np.uint8)

tabla_medias = encontrar_contornos()

centroides, data, asignaciones = kmeans(tabla_medias,6)

# Crear una gráfica 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=asignaciones, cmap='viridis')
ax.scatter(centroides[:, 0], centroides[:, 1], centroides[:, 2], marker='x', s=200, linewidths=3, color='red')
ax.set_xlabel("B")
ax.set_ylabel("G")
ax.set_zlabel("R")
ax.set_title("Grafica k-means")

plt.show()