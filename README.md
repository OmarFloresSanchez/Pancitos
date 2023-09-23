# Equipo: Pancitos 

## Practica 1.1
![Status](https://img.shields.io/badge/STATUS-FINALIZADO-red)

El objetivo es practicar la programacion colaborativa 

> [!NOTE] 
> profe, este readme lo editamos el 10 de septiembre jeje ya estaba lo que nos habia pedido en la practica pero andabamos experimetando un poco con los estilos y ps ahora se ve mas bonito jeje tambien pusimos lo de la primera practica en un folder, solo por la organizacion 

### Integrantes:
* Omar Flores Sanchez - [OmarFloresSanchez](https://github.com/OmarFloresSanchez)
* Valeria Jahzeel Castañon Hernandez - [ValeriaJahzeel](https://github.com/ValeriaJahzeel)
* Edkir Uriel Nava Mendez - [EdkirM](https://github.com/EdkirM)
* Eliud Roman Gutierrez Perez - [eliudroman](https://github.com/eliudroman)

## Practica 1.2
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Status](https://img.shields.io/badge/STATUS-FINALIZADO-red)

El objetivo es empezar con un análisis digital básico utilizando OpenCV

### Instrucciones
* Busquen una imagen con transiciones de colores notorias y leanla con OpenCV
* Creen una función que genere un histograma pero considerando todos los canales de la imagen
* De forma manual (ustedes definan el área), generen una subventana de la imagen, con la misma hagan lo siguiente:
     * Conviértanla a escala de grises (NTSC formula: 0.299 ∙ Red + 0.587 ∙ Green + 0.114 ∙ Blue)
     * Muestren su histograma
     * De forma aleatorio consideren 5 filas y grafiquen sus valores de intensidad para analizar las transiciones


## Practica 1.3
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Status](https://img.shields.io/badge/STATUS-EN/DESARROLLO-red)

Objetivo: Programar la transformada de Hough sin utililizar las librerias de python

### Instrucciones
* Ocupando la transformada de Hough (codificarla, no ocupar funciones) realicen la detección de líneas sobre un subconjunto aleatorio de 50 imágenes del conjunto de datos kitti
* La salida es una imagen donde se marcan las líneas detectadas y una imagen del espacio de Hough donde se tiene que notar que existen varios puntos de intersección que van a representar las líneas
* Ocupando el algoritmo de etiquetado de componentes conectados, identificar los componentes presentes en una muestra de 50 imágenes del conjunto de datos de Artificial Mercosur License Plates
* En la imagen de salida colorear los componentes que se identifiquen de distintos colores