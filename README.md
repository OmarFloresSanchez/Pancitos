# Equipo: Pancitos 

> [!NOTE] 
> Se ha creado una serie de carpetas que contienen todos los programas realizados y por realizar.
> Esta carpeta se llama main y tiene las subcarpetas bordes, detectores_formas, formas_binarias, segmentacion y utilidades

## Practica 1.1 - Programación colaborativa
![Status](https://img.shields.io/badge/STATUS-FINALIZADO-red)

El objetivo es practicar la programacion colaborativa 

### Integrantes:
* Omar Flores Sanchez - [OmarFloresSanchez](https://github.com/OmarFloresSanchez)
* Valeria Jahzeel Castañon Hernandez - [ValeriaJahzeel](https://github.com/ValeriaJahzeel)
* Edkir Uriel Nava Mendez - [EdkirM](https://github.com/EdkirM)
* Eliud Roman Gutierrez Perez - [eliudroman](https://github.com/eliudroman)

## Practica 1.2 - Histograma y conversion a grises
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


## Practica 1.3 - Transformada de Hough
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Status](https://img.shields.io/badge/STATUS-FINALIZADO-red     )    

Objetivo: Programar la transformada de Hough sin utililizar las librerias de python

### Instrucciones
* Ocupando la transformada de Hough (codificarla, no ocupar funciones) realicen la detección de líneas sobre un subconjunto aleatorio de 50 imágenes del conjunto de datos kitti
* La salida es una imagen donde se marcan las líneas detectadas y una imagen del espacio de Hough donde se tiene que notar que existen varios puntos de intersección que van a representar las líneas
* Ocupando el algoritmo de etiquetado de componentes conectados, identificar los componentes presentes en una muestra de 50 imágenes del conjunto de datos de Artificial Mercosur License Plates
* En la imagen de salida colorear los componentes que se identifiquen de distintos colores

## Practica 1.4 - Umbralizacion: global, Otsu, Bernsen
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Status](https://img.shields.io/badge/STATUS-FINALIZADO-red)

Objetivo: Desarrollar y aplicar en casos específicos las diversas técnicas de umbralización que fueron revisadas en clase.

### Instrucciones
Ocupando el lenguaje Python en el IDE de su preferencia, realizar el desarrollo de un programa donde implementen (a mano) las siguientes técnicas
de umbralización:
* Umbralización global
* Umbralización global por el método de Otsu
* Umbralización local adaptativa por el método de Bernsen
Todas las técnicas reciben como entrada imágenes de un solo canal, es decir, en escala de grises. Las imágenes que interesa que chequen vienen adjuntada en la actividad.

## Practica 2.1 - Segmentacion: crecimiento de región y k-medias
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Status](https://img.shields.io/badge/STATUS-FINALIZADO-red)

Objetivo: Desarrollar y aplicar en casos específicos las diversas técnicas de segmentación que fueron revisadas en clase.

### Instrucciones
Ocupando el lenguaje Python en el IDE de su preferencia, realizar el desarrollo de un programa donde implementen (a mano) las siguientes técnicas
de umbralización:
* Segmentacion por crecimiento de region
* Segmentación por cluster por el método de k-medias

## Practica 2.2 - Moore boundary tracing algorithm y cadenas de Freeman
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Status](https://img.shields.io/badge/STATUS-FINALIZADO-red)

Objetivo: Desarrollar y aplicar en casos específicos las diversas técnicas de preprocesamiento de límites (boundaries) que fueron revisadas en clase.

### Instrucciones
Ocupando el lenguaje Python en el IDE de su preferencia, realizar el desarrollo de un programa donde implementen (a mano) las siguientes técnicas de segmentación:
* Algoritmo de seguimiento de límites (Moore boundary tracing algorithm).
* Algoritmo de códigos de cadenas. Aquí se asume que se tienen imágenes con curvas cerradas y simples. Ocupen conectividad-4 y conectividad-8.

## Proyecto de 2° parcial - Clasificación de datos usando técnicas vistas en clase
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Status](https://img.shields.io/badge/STATUS-FINALIZADO-red)

Objetivo: Realizar una investigación de forma parcial sobre los temas que se han revisado en el apartado de la descripción de objetos presentes en una imagen mediante la región de los bordes/límites (boundaries).

### Instrucciones
Elijan un conjunto de datos (puede ser MNIST o CIFAR 10 o algún otro) y hagan una caracterización de los objetos ocupando descriptores de bordes.
1. Procesar datos
2. Ocupar algoritmos que han implementado en prácticas pasadas (Tracing, Freeman, MPP) o implementar alguno de los platicados al fina (Signatures, Thinning, Fourier) para generar los descriptores.
3. El o los algoritmos empleados deben de generar descriptores invariantes ante la transformación de la rotación y el escalamiento de las imágenes, para ello deben de generar estas transformaciones sobre el conjunto de datos. Ustedes proponen el ángulo de rotación y la proporción del escalamiento. Al final por cada imagen terminamos con tres: la original, la rotada y la escalada.
4. Una vez con los descriptores, analizar si existen similitudes entre los los datos que nos puedan indicar que a través de ellos podemos hacer un reconocimiento de los objetos del conjunto de datos. Tal vez pueden hacer clustering con los descriptores, tal vez pueden graficar los descriptores super puestos en los objetos o algo más.
5. Para probar pueden ocupar un subconjunto del conjunto de datos, por lo menos un objeto de cada clase presente. Por ejemplo, si consideran MNIST, un objeto de cada clase serían 9 imágenes, después de aplicar las transformaciones, terminarían con 27.

## Práctica 3.1 - Clasificador con PCA y T-SNE
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Status](https://img.shields.io/badge/STATUS-FINALIZADO-red)

Objetivo: Desarrollar y aplicar el método de clasificación de mínima distancia.

### Instrucciones
Ocupando el lenguaje Python en el IDE de su preferencia, realizar el
desarrollo de un programa donde implementen (a mano) el método de
clasificación de mínima distancia, para ello considerar lo siguiente:
* Desarrollar el método de clasificación como si fuera una clase de scikit-learn,
lo que significa que vamos a hacer la abstracción del método. Lo básico que
llevan estas implementaciones son los parámetros necesarios del método a
forma de atributos y dos métodos, fit (que realiza el entrenamiento) y predict
(que realiza una predicción/inferencia).
* En el método de fit aplicar debemos de realizar el cálculo de centroides y
distancias (euclidiana) donde se van a crear los límites de decisión
(almacenar esta información). Lo que debemos de recibir es el conjunto de
datos y con ellos trabajar.
* El método predict hará la evaluación de un conjunto de datos de prueba con
el límite de decisión, lo que debe de retornar es un vector con los índices de
las clases predichas.
* Con el vector retornado de predict, ocupen scikit-learn para calcular el
accuracy y también su matriz de confusión.
* Consideren el método de holdout para la preparación de los datos con una
proporción de 80%-20% para los subconjuntos de entrenamiento y prueba,
respectivamente.

## Práctica 3.2 - SIFT
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Status](https://img.shields.io/badge/STATUS-FINALIZADO-red)

Objetivo: Desarrollar y aplicar el método SIFT para la extracción de descriptores y
también para la fase de pareo de puntos clave entre dos imágenes.

### Instrucciones
Ocupando el lenguaje Python en el IDE de su preferencia, realizar el desarrollo de un programa donde implementen (a mano) el método de SIFT, para
ello considerar lo siguiente:
* En la implementación busquen ser modulares y creen funciones donde se aprecie que se hace cada uno de los pasos del algoritmo de SIFT
(Construcción de espacio de escalas, Localización de puntos clave, Asignación de orientación, Descriptor de puntos clave). No hay problema si
dentro de una función llaman a otras funciones, se entiende que es para no repetir código.
* Cada uno de los pasos del algoritmo nos debe de dar un resultado que debemos de poder visualizar.
* Finalmente, sabemos que no es parte del algoritmo, pero se espera que implementen el pareo (unión) de puntos clave entre nuestro template y la imagen donde queremos ubicar el objeto.