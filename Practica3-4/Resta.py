def resta(referencia, actual):
     ref = cv2.imread(referencia, cv2.IMREAD_GRAYSCALE)
     act = cv2.imread(actual, cv2.IMREAD_GRAYSCALE)

     alto, ancho = ref.shape

     resta = np.zeros((alto, ancho), dtype=np.int32)
     for i in range(alto):
          for j in range(ancho):
               resta[i, j] = abs(int(act[i, j]) - int(ref[i, j]))

               # se asegura de que no se salgan de los limites
               if resta[i,j] > 255:
                    resta[i,j] = 255
     
     img_resta = Image.fromarray(np.uint8(resta))

     cv2.imwrite('resta.jpg',resta)


     plt.imshow(img_resta, cmap='gray')

     return resta


ressta = resta('video3/frame30.jpg', 'video3/frame30.jpg')
