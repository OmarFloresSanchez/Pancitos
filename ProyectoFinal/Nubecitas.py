#------------/////////////////////////////////////////////////+*+*__BIBLIOTECAS__*+*+/////////////////////////////////////////////////--------------#
import cv2
import numpy as np
import matplotlib.pyplot as plt
#------------/////////////////////////////////////////////////+*+*__COSITAS__*+*+/////////////////////////////////////////////////--------------#

#Captura del video
cap = cv2.VideoCapture("vtest.avi")
#Primer cuadro del video
ret, frame1 = cap.read()
#Cositas del tutorial
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
#Kernel
kernel = np.ones((7,7),np.uint8)
#------------/////////////////////////////////////////////////+*+*__FUNCION CHIPOCHES__*+*+/////////////////////////////////////////////////--------------#

def descriptor(original,image_to_compare):
    x=0
    y=0
    if original.shape == image_to_compare.shape:
        #print('Las imagenes tiene el mismo tamaño y canal')
        difference = cv2.subtract(original, image_to_compare)
        b, g, r = cv2.split(difference)
        #Se junta en x
        x=cv2.countNonZero(b)
        #print(cv2.countNonZero(b))
##        if (cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
##            print('Las imagenes son completamente iguales')
##        else: 
##            print('Las imagenes no son iguales')
    shift = cv2.xfeatures2d.SIFT_create()
    kp_1, desc_1 = shift.detectAndCompute(original, None)
    kp_2, desc_2 = shift.detectAndCompute(image_to_compare, None)
    #print("Keypoints 1st image", str(len(kp_1)))
    #print("Keypoints 2st image", str(len(kp_2)))
    #Se junta en y
    y=len(kp_2)
    index_params = dict(algorithm=0, trees=5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(desc_1, desc_2, k=2)
    good_points = []
    for m, n in matches:
        if m.distance < 0.6*n.distance:
            good_points.append(m)
    number_keypoints = 0
    if (len(kp_1) <= len(kp_2)):
        number_keypoints = len(kp_1)
    else:
        number_keypoints = len(kp_2)
    #print("GOOD matches",len(good_points))
    #print("Que tan bueno es el match", len(good_points) / number_keypoints * 100, "%")
    result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)
##    cv2.imshow("Result", cv2.resize(result, None, fx = 0.4, fy=0.4))
##    cv2.imwrite("Feature_matching.jpg", result)
##    cv2.imshow("Original", original)
##    cv2.imshow("Duplicate", image_to_compare)
##    cv2.waitKey(0)
##    cv2.destroyAllWindows()
    return x,y
 #------------/////////////////////////////////////////////////+*+*__CICLO DEL VIDEO__*+*+/////////////////////////////////////////////////--------------#

#Contador
cont=0
while(1):
  #Obtencion de frames
  ret, frame2 = cap.read()
  #Engrisacion
  next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
  #Flujo de nuvecitas
  flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
   #Cositas nuvescas jsjs
  mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
  hsv[...,0] = ang*180/np.pi/2
  hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
  rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
  
  #---////////*-*-*_AQUI YA SE PUEDE CHAMBIAR_*-*-*//////////---------#
  
  #Engrizacion pero de las nubecitas
  gris=cv2.cvtColor(rgb,cv2.COLOR_BGR2GRAY)
  #Binarizacion
  ret,binario = cv2.threshold(gris,20,255,cv2.THRESH_BINARY)
  #Contornos de nubes
  #cent=cv2.findContours(binario, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
  #Dilatacion
  #dilatacion = cv2.dilate(binario,kernel,iterations = 1)
  #Contorno
  #contorno=dilatacion-binario
  #Guardado del cuadro
  if cont% 2 == 0:
    nombre=str(cont/2)
    nombre+="c.jpg"
    nombre2=str(cont/2)
    nombre2+="b.jpg"
    cv2.imwrite(nombre, frame2)
    cv2.imwrite(nombre2, binario)
  #Enseñacion de las imagenes
  #cv2.imshow('frame2',rgb)
  #cv2.imshow('frame23',frame2)
##  cv2.imshow('bn', binario)
##  cv2.imshow('dil', contorno)
##  #Velocidad de video
##  velocidad=20
##  #Detencion del video
##  k = cv2.waitKey(30) & 0xFF
##  if k == 27:
##    break
##  elif k == ord('s'):
##    cv2.imwrite('opticalfb.png',frame2)
##    cv2.imwrite('opticalhsv.png',rgb)
  prvs = next
  #Ahumenta la cuenta
  cont+=1
#------------/////////////////////////////////////////////////+*+*__FUERA DEL VIDEO__*+*+/////////////////////////////////////////////////--------------#

#Nomas se destruye el video 
cap.release()
cv2.destroyAllWindows()

"""
#------------/////////////////////////////////////////////////+*+*__IMAGENES__*+*+/////////////////////////////////////////////////--------------

#Lectura
foto1=cv2.imread('0.jpg')
foto2=cv2.imread('2.jpg')
foto3=cv2.imread('4.jpg')
foto4=cv2.imread('6.jpg')
#Promedio
fotos=foto1+foto2+foto3+foto4
fotos=fotos/4
descriptor(foto2,foto4)
##descriptor(fotos,foto2)
##descriptor(fotos,foto3)
##descriptor(fotos,foto4)

#Se enseña
cv2.imshow('Pokemon XY',fotos)
#Se quita
cv2.waitKey(0);
cv2.destroyAllWindows()
#Binarizacion
ret,binario = cv2.threshold(fotos,20,255,cv2.THRESH_BINARY)
#Kernel
kernel = np.ones((7,7),np.uint8)
#Dilatacion
dilatacion = cv2.dilate(fotos,kernel,iterations = 1)
#Contorno
contorno=dilatacion-binario
#Binarizacion
ret,binario = cv2.threshold(contorno,5,255,cv2.THRESH_BINARY)
#Kernel
kernel = np.ones((3,3),np.uint8)
#Apertura
apertura=cv2.morphologyEx(binario, cv2.MORPH_OPEN, kernel)
#Se enseña
cv2.imshow('Pokemon XY',apertura)
#Se quita
cv2.waitKey(0);
cv2.destroyAllWindows()

"""
#------------/////////////////////////////////////////////////+*+*__ MEJORES IMAGENES__*+*+/////////////////////////////////////////////////--------------

base1=cv2.imread('0.0b.jpg')
base2=cv2.imread('0.0c.jpg')
bases=base1*base2
#Valores
x=[]
y=[]
for i in range(200):
    #Se habren fotos
    #print(i+1)
    nombre=str(i+1)
    nombre1=nombre+".0b.jpg"
    foto1=cv2.imread(nombre1)
    nombre2=nombre+".0c.jpg"
    foto2=cv2.imread(nombre2)
    multi=foto1*foto2
    #Descriptor
    h,k=descriptor(bases,multi)
    x.append(h)
    y.append(k)
#Impresiones
print(x)
print(y)
plt.scatter(x,y,color='hotpink')
plt.show()



