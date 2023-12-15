def umbralizacion_bernsen(imagen, kernel, umbral):
    alto, ancho = imagen.shape  
    resultado = np.zeros_like(imagen)   # hace una matriz de 0 del tamaño de la imagen

    radio = kernel // 2    # hace una division con un resultado entero para saber el radio del kernel

    for x in range(radio, alto - radio): # se hace la convolucion de la ventana
        for y in range(radio, ancho - radio):
            ventana = imagen[x - radio:x + radio + 1,
                             y - radio:y + radio + 1]
            
            min_pixel = np.min(ventana) # obtiene el minimo pixel 
            max_pixel = np.max(ventana) # obtiene el maximo pixel 

            if max_pixel - min_pixel <= umbral: # si la suma de ellos es menor al umbral...
                resultado[x, y] = 0
            else:
                resultado[x, y] = 255

    img_bernsen = Image.fromarray(resultado)

    cv2.imwrite('bernsen.jpg',resultado)

    plt.imshow(img_bernsen, cmap='gray')

    return resultado

umbralizada = umbralizacion_bernsen(ressta, 5, 45) 

kernel = np.ones((2, 2), np.uint8)

umbralizada = umbralizada.astype(np.uint8)

erosion = cv2.erode(umbralizada, kernel, iterations = 1)

plt.imshow(erosion, cmap='gray')

dilatacion = cv2.dilate(umbralizada, kernel, iterations = 3)

plt.imshow(dilatacion, cmap='gray')

apertura = cv2.morphologyEx(umbralizada, cv2.MORPH_OPEN, kernel)
plt.imshow(apertura, cmap='gray')

clausura = cv2.morphologyEx(umbralizada, cv2.MORPH_CLOSE, kernel)
plt.imshow(clausura, cmap='gray') 
