def umbralizacionOtsu(imagen):
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

    print("Otsu: ", final)

    return imagen_binaria


# ----- LLAMADO DE LAS FUNCIONES -----
imagen = cv2.imread(foto1, 0)   # lee la imagen en escala de grises

otsu = umbralizacionOtsu(imagen)  # guarda la imagen que resulta de ostu

imgOtsu = Image.fromarray(otsu)    # pasa el arreglo a imagen

# Muestra la imagen original y la imagen umbralizada
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(imagen, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(imgOtsu, cmap='gray')
plt.title('Imagen Umbralizada (Otsu)')
plt.axis('off')

plt.show()
