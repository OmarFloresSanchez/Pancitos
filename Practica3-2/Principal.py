# Cargar imágenes
img1 = cv.imread('img1.jpg')
img2 = cv.imread('img2.jpg')

img2 = cv.resize(img1, (int(img1.shape[1]/2), int(img1.shape[0]/2)))
img3 = cv.resize(img1, (int(img1.shape[1]/4), int(img1.shape[0]/4)))
img4 = cv.resize(img1, (int(img1.shape[1]/8), int(img1.shape[0]/8)))

# Suavizados
blur1_1 = cv.GaussianBlur(img1, (5,5), 0)
blur1_2 = cv.GaussianBlur(blur1_1, (5,5), 0)
blur1_3 = cv.GaussianBlur(blur1_2, (5,5), 0)
blur1_4 = cv.GaussianBlur(blur1_3, (5,5), 0)

blur2_1 = cv.GaussianBlur(img2, (5,5), 0)
blur2_2 = cv.GaussianBlur(blur2_1, (5,5), 0)
blur2_3 = cv.GaussianBlur(blur2_2, (5,5), 0)
blur2_4 = cv.GaussianBlur(blur2_3, (5,5), 0)

blur3_1 = cv.GaussianBlur(img3, (5,5), 0)
blur3_2 = cv.GaussianBlur(blur3_1, (5,5), 0)
blur3_3 = cv.GaussianBlur(blur3_2, (5,5), 0)
blur3_4 = cv.GaussianBlur(blur3_3, (5,5), 0)

blur4_1 = cv.GaussianBlur(img4, (5,5), 0)
blur4_2 = cv.GaussianBlur(blur4_1, (5,5), 0)
blur4_3 = cv.GaussianBlur(blur4_2, (5,5), 0)
blur4_4 = cv.GaussianBlur(blur4_3, (5,5), 0)

# Titulos para las escalas
imagenes_escalas = [img1, blur1_1, blur1_2, blur1_3, blur1_4, img2, blur2_1, blur2_2, blur2_3, blur2_4, img3, blur3_1, blur3_2, blur3_3, blur3_4, img4, blur4_1, blur4_2, blur4_3, blur4_4]
titulos_escalas = ['Primer octava ->', 'Blur1_1', 'Blur1_2', 'Blur1_3', 'Blur1_4', 'Segunda octava ->', 'Blur2_1', 'Blur2_2', 'Blur2_3', 'Blur2_4', 'Tercer octava ->', 'Blur3_1', 'Blur3_2', 'Blur3_3', 'Blur3_4', 'Cuarta octava ->', 'Blur4_1', 'Blur4_2', 'Blur4_3', 'Blur4_4']

# Mostrar escalas
mostrarImagenes(imagenes_escalas, titulos_escalas, 4, 5, suptitle='Espacio de escala')

# Restas de Gaussianas
gau1_1 = img1 - blur1_1
gau1_2 = blur1_1 - blur1_2
gau1_3 = blur1_2 - blur1_3
gau1_4 = blur1_3 - blur1_4

gau2_1 = img2 - blur2_1
gau2_2 = blur2_1 - blur2_2
gau2_3 = blur2_2 - blur2_3
gau2_4 = blur2_3 - blur2_4

gau3_1 = img3 - blur3_1
gau3_2 = blur3_1 - blur3_2
gau3_3 = blur3_2 - blur3_3
gau3_4 = blur3_3 - blur3_4

gau4_1 = img4 - blur4_1
gau4_2 = blur4_1 - blur4_2
gau4_3 = blur4_2 - blur4_3
gau4_4 = blur4_3 - blur4_4

# Nombres de los gaussianos
gau_images = [gau1_1, gau1_2, gau1_3, gau1_4, gau2_1, gau2_2, gau2_3, gau2_4, gau3_1, gau3_2, gau3_3, gau3_4, gau4_1, gau4_2, gau4_3, gau4_4]
gau_titles = ['Gau1_1', 'Gau1_2', 'Gau1_3', 'Gau1_4', 'Gau2_1', 'Gau2_2', 'Gau2_3', 'Gau2_4', 'Gau3_1', 'Gau3_2', 'Gau3_3', 'Gau3_4', 'Gau4_1', 'Gau4_2', 'Gau4_3', 'Gau4_4']

# Mostrar gaussianas
mostrarImagenes(gau_images, gau_titles, 4, 4, figsize=(16, 16), suptitle='Diferencias de Gaussianas')

# Calcular ángulos y mostrar el histograma
angulos = calcularGradientes(img2)
histograma(angulos)

img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

sift = cv.xfeatures2d.SIFT_create()

keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)

len(keypoints_1), len(keypoints_2)
bf = cv.BFMatcher(cv.NORM_L1, crossCheck=True)

matches = bf.match(descriptors_1,descriptors_2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[:50], img2, flags=2)
plt.imshow(img3)
plt.show()
