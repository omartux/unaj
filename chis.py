# -*- coding: utf-8 -*-
"""
UNAJ
Omar Castillo Alarcon 
aka Omartux
gnu.omar@gmail.com
"""
import cv2 as cv
import numpy as np
from datetime import date, datetime
import os
import time
import statistics as stat


print ("Iniciando ")
time.sleep(1)


# cv.namedWindow('control', cv.WINDOW_NORMAL)
# cv.resizeWindow('control', 640,480)

hoy = date.today()
ahora = datetime.now()
tiempo_actual = ahora.strftime("%H:%M:%S")
# Objetivos : 
# - Leer la carpeta de imagenes
# - Iterar las imagenes en la carpeta
# - Cada imagen debe detectarse su borde
# - Cada imagen debe detectarse sus valores de componentes de color
# - Guardar los datos en un archivo csv


print (hoy)
print (ahora)
print (tiempo_actual)

archivo = open('medidas.csv', "w+")
cadena = ('dia'+";"+'tiempo_actual'+";"+'archivo'+";"
          +'medH'+";"+'medS'+";"+'medV'+";"
          +'medB'+";"+'medG'+";"+'medR'+";"
          +'medL'+";"+'medA'+";"+'medBB'+";"
          +'medY'+";"+'medCB'+";"+'medCR'+";"
          +'meH'+";"+'meS'+";"+'meV'+";"
          +'meB'+";"+'meG'+";"+'meR'+";"
          +'meL'+";"+'meA'+";"+'meBB'+";"
          +'meY'+";"+'meCB'+";"+'meCR'+"\n") 

archivo.write(cadena)
archivo.close()

carpeta = os.getcwd()
fotos = str(carpeta+"\\fotos")
print ("entrando en ... ",fotos)

for filename in os.listdir(fotos):
    if filename.endswith(".jpg") or filename.endswith(".JPG"):
        print (filename)
        entrada = './fotos/'+filename
        print (entrada)
        frame = cv.imread(entrada,cv.IMREAD_UNCHANGED)
        dimensiones = frame.shape
        h = frame.shape[0]
        w = frame.shape[1]
        ch = frame.shape[2]
        print (h,w,ch)
        segmentacion = frame.copy()
        
        
        bgr = frame.copy()

        bgr = cv.resize(bgr, (1280,960))
        normal = bgr.copy()

        gray = cv.cvtColor(bgr, cv.COLOR_BGR2GRAY)

        
        gray = cv.GaussianBlur(gray, (11, 11), 0)
        mediana = np.median(gray)
        
      
        canny_inf = int(0.33*mediana) 
        canny_sup = int(1.33*mediana)
        
        print (int(mediana), canny_inf, canny_sup)
        
        
        kernel = 9
        
        canny = cv.Canny(gray, canny_inf, canny_sup, kernel)
            
        (contornos, _) = cv.findContours(canny.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        
        grosor = 6
        
        
        if len(contornos) > 10:
            path1 = ".\errores\\" 
            name1 = 'error_'+filename
            cv.imwrite(str(path1+name1), canny)
            cv.imwrite(str(path1+'g_'+name1), gray)
    

        if len(contornos) > 0 and len(contornos) < 10:
            canny = cv.drawContours(canny, contornos[0], -1, (255, 255, 255), thickness=grosor)
            thresh = cv.threshold(canny, 5, 255, cv.THRESH_BINARY)[1]
            contours = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
            contours = contours[0] if len(contours) == 2 else contours[1]
            big_contour = max(contours, key=cv.contourArea)
    
            mask = np.zeros(normal.shape[:2], np.uint8)
            mask = cv.drawContours(mask, [big_contour], 0, (255, 255, 255), cv.FILLED)


            result = cv.bitwise_and(normal, normal, mask=mask)
        
            
            hsv = cv.cvtColor(result, cv.COLOR_BGR2HSV)
            bgr = result.copy()
            lab = cv.cvtColor(result, cv.COLOR_BGR2LAB)
            ycbcr = cv.cvtColor(result, cv.COLOR_BGR2YCR_CB)
            
            h, s, v = cv.split(hsv)
            b, g, r = cv.split(bgr)
            l, a, bb = cv.split(lab)
            y, cb, cr = cv.split(ycbcr)
            
            #chancada de salidas para eliminar info
            h = cv.bitwise_and(h, h, mask=mask)
            s = cv.bitwise_and(s, s, mask=mask)
            v = cv.bitwise_and(v, v, mask=mask)
            
            b = cv.bitwise_and(b, b, mask=mask)
            g = cv.bitwise_and(g, g, mask=mask)
            r = cv.bitwise_and(r, r, mask=mask)
            
            l = cv.bitwise_and(l, l, mask=mask)
            a = cv.bitwise_and(a, a, mask=mask)
            bb = cv.bitwise_and(bb, bb, mask=mask)
    
            y = cv.bitwise_and(y, y, mask=mask)
            cb = cv.bitwise_and(cb, cb, mask=mask)
            cr = cv.bitwise_and(cr, cr, mask=mask)

            #flatten y ordenar h
            vector_h = h.flatten()
            newVector_h=[]
            for i in vector_h:    
                if i>0:
                    newVector_h.append(i)

            #flatten y ordenar s
            vector_s = s.flatten()
            newVector_s=[]
            for i in vector_s:    
                if i>0:
                    newVector_s.append(i)

            #flatten y ordenar v
            vector_v = v.flatten()
            newVector_v=[]
            for i in vector_v:    
                if i>0:
                    newVector_v.append(i)
                    
            #flatten y ordenar b
            vector_b = b.flatten()
            newVector_b=[]
            for i in vector_b:    
                if i>0:
                    newVector_b.append(i)

            #flatten y ordenar g
            vector_g = g.flatten()
            newVector_g=[]
            for i in vector_g:    
                if i>0:
                    newVector_g.append(i)
                    
            
            #flatten y ordenar r
            vector_r = r.flatten()
            newVector_r=[]
            for i in vector_r:    
                if i>0:
                    newVector_r.append(i)


            #flatten y ordenar l
            vector_l = l.flatten()
            newVector_l=[]
            for i in vector_l:    
                if i>0:
                    newVector_l.append(i)


            #flatten y ordenar a
            vector_a = a.flatten()
            newVector_a=[]
            for i in vector_a:    
                if i>0:
                    newVector_a.append(i)


            #flatten y ordenar bb
            vector_bb = bb.flatten()
            newVector_bb=[]
            for i in vector_bb:    
                if i>0:
                    newVector_bb.append(i)

            #flatten y ordenar y
            vector_y = y.flatten()
            newVector_y=[]
            for i in vector_y:    
                if i>0:
                    newVector_y.append(i)

            #flatten y ordenar cb
            vector_cb = cb.flatten()
            newVector_cb=[]
            for i in vector_cb:    
                if i>0:
                    newVector_cb.append(i)

            #flatten y ordenar cr
            vector_cr = cr.flatten()
            newVector_cr=[]
            for i in vector_cr:    
                if i>0:
                    newVector_cr.append(i)
                    
            #moda = stat.mode(ele.flatten())
            
            #flatten y ordenar h
            
            # vector_h = h.flatten()
            # cont_h = 0
            # newVector_h=[]
            # while cont_h < len(vector_h):
            #     if
            #     newVector_h
                
            
            # for i in vector_h:    
            #     if i>0:
            #         newVector_h.append(i)
    
            medH = np.median(newVector_h)
            medS = np.median(newVector_s)
            medV = np.median(newVector_v)
            
            medB = np.median(newVector_b)
            medG = np.median(newVector_g)
            medR = np.median(newVector_r)
            
            medL = np.median(newVector_l)
            medA = np.median(newVector_a)
            medBB = np.median(newVector_bb)
        
            medY = np.median(newVector_y)
            medCB = np.median(newVector_cb)
            medCR = np.median(newVector_cr)
            #********************
            meH = np.mean(newVector_h)
            meS = np.mean(newVector_s)
            meV = np.mean(newVector_v)
            
            meB = np.mean(newVector_b)
            meG = np.mean(newVector_g)
            meR = np.mean(newVector_r)
            
            meL = np.mean(newVector_l)
            meA = np.mean(newVector_a)
            meBB = np.mean(newVector_bb)
             
            meY = np.mean(newVector_y)
            meCB = np.mean(newVector_cb)
            meCR = np.mean(newVector_cr)
            
            meH = np.round(meH,2)
            meS = np.round(meS,2)
            meV = np.round(meV,2)
        
            meB = np.round(meB,2)
            meG = np.round(meG,2)
            meR = np.round(meR,2)
       
            meL = np.round(meL,2)
            meA = np.round(meA,2)
            meBB = np.round(meBB,2)
            
            meY = np.round(meY,2)
            meCB = np.round(meCB,2)
            meCR = np.round(meCR,2)  
            
            #guardado de los resultados
            hoy = date.today()
            ahora = datetime.now()
            tiempo_actual = ahora.strftime("%H:%M:%S")
            
            print(medH, medS, medV, medB, medG, medR, medL, medA, medBB, medY, medCB, medCR)
            print(meH, meS, meV, meB, meG, meR, meL, meA, meBB, meY, meCB, meCR)
            
            #titulos
            archivo = open('medidas.csv', "a")
            cadena = (str(hoy)+";"+str(tiempo_actual)+";"+str(filename)+";"
                      +str(medH)+";"+str(medS)+";"+str(medV)+";"
                      +str(medB)+";"+str(medG)+";"+str(medR)+";"
                      +str(medL)+";"+str(medA)+";"+str(medBB)+";"
                      +str(medY)+";"+str(medCB)+";"+str(medCR)+";"
                      +str(meH)+";"+str(meS)+";"+str(meV)+";"
                      +str(meB)+";"+str(meG)+";"+str(meR)+";"
                      +str(meL)+";"+str(meA)+";"+str(meBB)+";"
                      +str(meY)+";"+str(meCB)+";"+str(meCR)+"\n") 
            archivo.write(cadena)
            archivo.close()
            
            path = ".\salida\\" 
            name = 'out_'+filename
            
            namel = 'l_'+filename
            namea = 'a_'+filename
            namebb = 'bb_'+filename
            
            nameh = 'h_'+filename
            names = 's_'+filename
            namev = 'v_'+filename
            
            nameb = 'b_'+filename
            nameg = 'g_'+filename
            namer = 'r_'+filename
            
            namey = 'y_'+filename
            namecb = 'cb_'+filename
            namecr = 'cr_'+filename
            
            
            
            cv.imwrite(str(path+name), result)
            cv.imwrite(str(path+namel), l)
            cv.imwrite(str(path+namea), a)
            cv.imwrite(str(path+namebb), bb)
            
            
            cv.imwrite(str(path+nameh), h)
            cv.imwrite(str(path+names), s)
            cv.imwrite(str(path+namev), v)

            cv.imwrite(str(path+nameb), b)
            cv.imwrite(str(path+nameg), g)
            cv.imwrite(str(path+namer), r)
            
            cv.imwrite(str(path+namey), y)
            cv.imwrite(str(path+namecb), cb)
            cv.imwrite(str(path+namecr), cr)            
        
            #cv.imwrite(str(path+'can_'+filename), canny)

cv.destroyAllWindows()
