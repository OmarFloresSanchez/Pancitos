#~*~*~*~*~*~*~*~*~*----------------------BIBLIOTECAS--------------------------*~*~*~*~*~*~*~*~*~*~*~*


from PIL import Image, ImageFilter
from numpy import array
import numpy as np
import matplotlib.pyplot as plt

#~*~*~*~*~*~*~*~*~*----------------------FUNCIONES--------------------------*~*~*~*~*~*~*~*~*~*~*~*


#EROSION

def erosion(array_U,kernel):
    
    dim = np.shape(array_U)
    erosion = np.zeros_like(array_U)
    kernel = kernel.astype(array_U.dtype)  
    for x in range(1, dim[0]-1):
        for y in range(1, dim[1]-1):
            if np.all(array_U[x-1:x+2, y-1:y+2] & kernel):
                erosion[x, y] = 255
    return erosion

#MNIST

def mnist(imagen):
   
    #Se suben imagenes
    foto=Image.open(imagen)
##    if(imagen=="img_4.jpg"):
##        print("Sies")
##        foto=foto.rotate(180)
    #Se cambian de tamaño
##    ancho=200
##    alto=200
##    foto=foto.resize((ancho, alto))
    
    #foto.show()
    #Se hace la matriz
    ker=np.array([[255, 255, 255], [255, 255, 255], [255, 255, 255]])
    #Dilatacion
    gris=foto.convert("L")

    #Umbralizacion
    for x in range(foto.size[0]):
        for y in range(foto.size[1]):
            #Si es mayor a 200 osea clarito
            if gris.getpixel((x,y))<50:
                #Lo pone negro
                gris.putpixel((x,y),(0))
            else:
                #Lo pone blanco
                gris.putpixel((x,y),(255))
    #gris.show()

    arr_g=np.array(gris)
    #Erosion
    e=erosion(arr_g, ker)
    er=Image.fromarray(e)
    #er.show()

    arr_g=np.array(gris)
    #Resta
    r=arr_g-e
    #Se enseña
    final=Image.fromarray(r)
    #final.show()

    prueva=np.array([[0, 0, 0, 0, 0, 0, 0],
                                              [0, 255, 255, 255, 255, 255, 0],
                                              [0, 255, 0, 0, 0, 255, 0],
                                              [0, 255, 0, 0, 0, 255, 0],
                                              [0, 255, 0, 0, 0, 255, 0],
                                              [0, 255, 255, 255, 255, 255, 0],
                                              [0, 0, 0, 0, 0, 0, 0]])
    imap=Image.fromarray(prueva)
    #imap.show()

    #~*~*~*~*~*~*~*~*~*----------------------CADENAS--------------------------*~*~*~*~*~*~*~*~*~*~*~*

    a=0
    inix=0
    iniy=0
    for x in range(final.size[0]):
        if(a==1):
            break
        for y in range(final.size[1]):
            if (a==0 and final.getpixel((x,y))==255):
                inix=x
                iniy=y
                a=1
    #3print("La primera coordenada es", inix,", ", iniy)

    #final=imap

    actx=0
    acty=0
    a=0
    mov=9
    cadena=[]
    b=0
    while(b==0):
        if(actx==inix and acty==iniy):
                b=1
                break
        #Si es el inicio
        if(a==0):
            if(final.getpixel((inix+1, iniy))==255 and mov!=4):
                cadena.append(0)
                final.putpixel((inix,iniy),0)
                actx=inix+1
                acty=iniy
                a=1
                mov=0
                #print("Actualx: ",actx,"Actualy: ",acty)
                #continue
        
                
            elif(final.getpixel((inix+1, iniy+1))==255 and mov!=5):
                cadena.append(1)
                final.putpixel((inix,iniy),0)
                actx=inix+1
                acty=iniy+1
                a=1
                mov=1
                #print("Actualx: ",actx,"Actualy: ",acty)
                #continue
                
            elif(final.getpixel((inix, iniy+1))==255 and mov!=6):
                cadena.append(2)
                final.putpixel((inix,iniy),0)
                actx=inix
                acty=iniy+1
                a=1
                mov=2
                #print("Actualx: ",actx,"Actualy: ",acty)
                #continue
                
            elif(final.getpixel((inix-1, iniy+1))==255 and mov!=7):
                cadena.append(3)
                final.putpixel((inix,iniy),0)
                actx=inix-1
                acty=iniy+1
                a=1
                mov=3
                #print("Actualx: ",actx,"Actualy: ",acty)
                #continue
                
            elif(final.getpixel((inix-1, iniy))==255 and mov!=0):
                cadena.append(4)
                final.putpixel((inix,iniy),0)
                actx=inix-1
                acty=iniy
                a=1
                mov=4
                #print("Actualx: ",actx,"Actualy: ",acty)
                #continue
                
            elif(final.getpixel((inix-1, iniy-1))==255 and mov!=1):
                cadena.append(5)
                final.putpixel((inix,iniy),0)
                actx=inix-1
                acty=iniy-1
                a=1
                mov=5
                #print("Actualx: ",actx,"Actualy: ",acty)
                #continue
                
            elif(final.getpixel((inix, iniy-1))==255 and mov!=2):
                cadena.append(6)
                final.putpixel((inix,iniy),0)
                actx=inix
                acty=iniy-1
                a=1
                mov=6
                #print("Actualx: ",actx,"Actualy: ",acty)
                #continue
            
            elif(final.getpixel((inix+1, iniy-1))==255 and mov!=3):
                cadena.append(7)
                final.putpixel((inix,iniy),0)
                actx=inix+1
                acty=iniy-1
                a=1
                mov=7
                #print("Actualx: ",actx,"Actualy: ",acty)
                #continue


                
        #Si no es el inicio----------------------------------------------
        if(a==1):
            if(final.getpixel((actx+1, acty))==255 and mov!=4):
                cadena.append(0)
                final.putpixel((actx, acty),0)
                actx=actx+1
                acty=acty
                mov=0
                #print("Actualx: ",actx,"Actualy: ",acty)
                #continue
                
            elif(final.getpixel((actx+1,acty+1))==255 and mov!=5):
                cadena.append(1)
                final.putpixel((actx, acty),0)
                actx=actx+1
                acty=acty+1
                mov=1
                #print("Actualx: ",actx,"Actualy: ",acty)
                #continue
                
            elif(final.getpixel((actx, acty+1))==255 and mov!=6):
                cadena.append(2)
                final.putpixel((actx, acty),0)
                actx=actx
                acty=acty+1
                mov=2
                #print("Actualx: ",actx,"Actualy: ",acty)
                #continue
                
            elif(final.getpixel((actx-1, acty+1))==255 and mov!=7):
                cadena.append(3)
                final.putpixel((actx, acty),0)
                actx=actx-1
                acty=acty+1
                mov=3
                #print("Actualx: ",actx,"Actualy: ",acty)
                #continue
                
            elif(final.getpixel((actx-1, acty))==255 and mov!=0):
                cadena.append(4)
                final.putpixel((actx, acty),0)
                actx=actx-1
                acty=acty
                mov=4
                #print("Actualx: ",actx,"Actualy: ",acty)
                #continue
                
            elif(final.getpixel((actx-1, acty-1))==255 and mov!=1):
                cadena.append(5)
                final.putpixel((actx, acty),0)
                actx=actx-1
                acty=acty-1
                mov=5
                #print("Actualx: ",actx,"Actualy: ",acty)
                #continue
                
            elif(final.getpixel((actx,acty-1))==255 and mov!=2):
                cadena.append(6)
                final.putpixel((actx, acty),0)
                actx=actx
                acty=acty-1
                mov=6
                #print("Actualx: ",actx,"Actualy: ",acty)
                #continue
            
            elif(final.getpixel((actx+1, acty-1))==255 and mov!=3):
                cadena.append(7)
                final.putpixel((actx, acty),0)
                actx=actx+1
                acty=acty-1
                mov=7
                #print("Actualx: ",actx,"Actualy: ",acty)
                #continue
            else:
                break
            
    ##print("La cadena es:")
    ##print(cadena)
    cadver=[]
    referencia=[0,1,2,3,4,5,6,7,0,1,2,3,4,5,6]
    for i in range (len(cadena)):
        if (i!=0):
            if (cadena[i]==cadena[i-1]):
                cadver.append(0)
            else:
                a=10
                b=10
                for j in range(len(referencia)):
                    if (referencia[j]==cadena[i]):
                        a=j
                    if (referencia[j]==cadena[i-1]):
                        b=j
                    if(a!=10 and b!=10):
                        break
                cadver.append(abs(a-b))
    return cadver

def contador(cadena):
    c01=0
    c11=0
    c21=0
    c31=0
    c41=0
    c51=0
    c61=0
    c71=0
    for i in cadena:
        if(i==0):
            c01+=1
        if(i==1):
            c11+=1
        if(i==2):
            c21+=1
        if(i==3):
            c31+=1
        if(i==4):
            c41+=1
        if(i==5):
            c51+=1
        if(i==6):
            c61+=1
        if(i==7):
            c71+=1
    conts=[c01,c11,c21,c31,c41,c51,c61,c71]
    return conts

def sumatoria(cont1, cont2, minimus):
    suma=0
    for i in range(8):
        if(abs(cont1[i]-cont2[i])<minimus):
            suma+=1
    return suma
#~*~*~*~*~*~*~*~*~*----------------------PRINCIPAL--------------------------*~*~*~*~*~*~*~*~*~*~*~*


ent0=mnist("img_1.jpg")
ent1=mnist("img_2.jpg")
ent2=mnist("img_22.jpg")
ent3=mnist("img_25.jpg")
ent4=mnist("img_115.jpg")
ent5=mnist("img_174.jpg")
ent6=mnist("img_45.jpg")
ent7=mnist("img_18.jpg")

prue=mnist("img_4.jpg")
print(prue)
#~*~*~*~*~*~*~*~*~*----------------------CLASIFICADOR--------------------------*~*~*~*~*~*~*~*~*~*~*~*

#Condatores
cen0=contador(ent0)
cen1=contador(ent1)
cen2=contador(ent2)
cen3=contador(ent3)
cen4=contador(ent4)
cen5=contador(ent5)
cen6=contador(ent6)
cen7=contador(ent7)

cpru=contador(prue)

#Minimos
pequeño=min(len(ent0),len(ent1),len(ent2),len(ent3),len(ent4),len(ent5),len(ent6),len(ent7),len(prue))

#Seleccionar
if(pequeño==len(ent0)):
    minimus=len(ent0)
if(pequeño==len(ent1)):
    minimus=len(ent1)
if(pequeño==len(ent2)):
    minimus=len(ent2)
if(pequeño==len(ent3)):
    minimus=len(ent3)
if(pequeño==len(ent4)):
    minimus=len(ent4)
if(pequeño==len(ent5)):
    minimus=len(ent5)
if(pequeño==len(ent6)):
    minimus=len(ent6)
if(pequeño==len(ent7)):
    minimus=len(ent7)
if(pequeño==len(prue)):
    minimus=len(prue)
minimus=minimus/10

suma0=sumatoria(cen0, cpru,minimus)
suma1=sumatoria(cen1, cpru,minimus)
suma2=sumatoria(cen2, cpru,minimus)
suma3=sumatoria(cen3, cpru,minimus)
suma4=sumatoria(cen4, cpru,minimus)
suma5=sumatoria(cen5, cpru,minimus)
suma6=sumatoria(cen6, cpru,minimus)
suma7=sumatoria(cen7, cpru,minimus)

##print(suma0)
##print(suma1)
##print(suma2)
##print(suma3)
##print(suma4)
##print(suma5)
##print(suma6)
##print(suma7)
umbral=6
if(suma0>=umbral):
    print("Es un 0")
if(suma1>=umbral):
    print("Es un 1")
if(suma2>=umbral):
    print("Es un 2")
if(suma3>=umbral):
    print("Es un 3")
if(suma4>=umbral):
    print("Es un 4")
if(suma5>=umbral):
    print("Es un 5")
if(suma6>=umbral):
    print("Es un 6")
if(suma7>=umbral):
    print("Es un 7")



    
        


