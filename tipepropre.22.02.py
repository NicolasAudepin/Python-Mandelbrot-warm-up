# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 10:45:19 2016

@author: Matthieu
"""

import cmath as c
from PIL import Image
import numpy as np
from colorsys import  hls_to_rgb
import matplotlib
import matplotlib.pyplot as plt
import marshal as m

#from image2gif import writeGif
"q désignera la qualité (la résolution) de l'image pour tous les programmes"
"il s'agit plus précisément du nombre de pixels par ligne et colonne"



"FONCTIONS AUXILIAIRES"



def convergence(c) :
    compteur=0
    z=c  
    if abs(1-(1-4*c)**0.5)<1 :
        return True  
    #point du cardioide principal
    if abs(c+1)<0.24 :
        return True
    #point du cardioide secondaire    
    while abs(z)<2 and compteur<100 :
        z=z*z+c
        compteur+=1
    if compteur==100 :
        return True
    return False       



def divergence(c):
    if abs(1-(1-4*c)**0.5)<1 :
        return 100
    if abs(c+1)<0.24 :
        return 100
    compteur=0
    z=c   
    while abs(z)<2 and compteur<100 :
        z=z*z+c
        compteur+=1
    return compteur



def divergence_précise(c,P):
    "P : nombre d'itérations pour voir si la suite est bornée"
    
    if abs(1-(1-4*c)**0.5)<1 :
        return P
    if abs(c+1)<0.24 :
        return P
    compteur=0
    z=c   
    while abs(z)<2 and compteur<P :
        z=z*z+c
        compteur+=1
    return compteur



def divergence_Julia(z,c,P):
    compteur=0   
    while abs(z)<2 and compteur<P :
        z=z*z+c
        compteur+=1
    return compteur 
    
    
    
def coeff_fourrier(f,z,nb):
      "f est la fréquence du signal"
      "nb désigne le nombre de terme de la somme du coefficient de fourrier"
      "retourne le coefficient de fourrier associé à la suite (z(n))"
      
      x=z
      S=z
      for i in range(nb):
          x=(z+(x**2))
          S+=x*np.exp(2*np.pi*complex(0,1)*f*i)
      return (abs(S))
      
      
      
def cofo(f,z,nb):
      "f est la fréquence du signal"
      "nb désigne le nombre de terme de la somme du coefficient de fourrier"
      "retourne le coefficient de fourrier associé à la suite (z(n))"
      
      x=z
      S=z
      for i in range(nb):
          x=(z+(x**2))
          S+=x*np.exp(-2*np.pi*complex(0,1)*f*i)
      return (abs(S)/nb)
          
def MH(f,nb=100,q=200):
      "f est la fréquence du signal"
      "nb désigne le nombre de terme de la somme du coefficient de fourrier"
      "retourne Mandelbrot après stimulation avec signal de fréquence f"
      
      M=Image.new("RGB",(q,q))
      for i in range (q):
         for j in range (q):
             if convergence(complex((4*i/q)-2.5,-(4*j/q)+2)):
                 e=cofo(f,complex((4*i/q)-2.5,-(4*j/q)+2),nb)
                 R=int(225*(e)**2)
                 G=int(225*(e)**2)
                 B=int(225*(e))
                 M.putpixel((i,j),(R,G,B))
             else:
                 M.putpixel((i,j),(40,20,0))
      M.save("Mandelbrot_harmonique_f="+str(f)+"_q="+str(q)+".png")
      M.show()
      del M        
    
    
"MANDELBROT"    
    
def Mandelbrot(q):
    M=[[[0,0,0] for i in range(q)] for j in range(q)]
    for i in range (q):
       for j in range (int(q/2)+1):
           if convergence(complex((4*i/q)-2.5,(4*j/q)-2)):
               M[i][j][0]=complex((4*i/q)-2.5,(4*j/q)-2)
               M[i][j][1]=divergence(complex((4*i/q)-2.5,(4*j/q)-2))
               M[i][j][2]=divergence_précise(complex((4*i/q)-2.5,(4*j/q)-2),200)
    m.dump(M,open("Mandelbrot"+str(q),'wb'))
    

    
def Mandelbrot_classique(q):
    "donne l'image sans degradés et la sauvegarde a coté du fichier"
    I=Image.new("RGB",(q,q))
    M=m.load(open("Mandelbrot"+str(q),"rb"))
    for i in range (q):
        for j in range (int(q/2)+1):
            if M[i][j][0]!=complex(0,0):
                I.putpixel((i,j),(150,155,155))                
                I.putpixel((i,q-j-1),(150,155,155))
            else :
                I.putpixel((i,j),(255,255,255))
                I.putpixel((i,q-j-1),(255,255,255))
    I.save("Mandelbrot_classique_q="+str(q)+".png")
    I.show()
    del I   

 
    
def Mandelbrot_dégradé(q):
    "pareil mais fait des dégradés en noir et blanc"    
    M=m.load(open("Mandelbrot"+str(q),"rb"))
    I=Image.new("RGB",(q,q))
    for i in range (q):
        for j in range (int(q/2)+1):
            a=M[i][j][1]
            n=int(225*a/100)
            I.putpixel((i,j),(n,n,n))
            I.putpixel((i,q-j-1),(n,n,n))
    I.save("Mandelbrot_rapide_q="+str(q)+".png")
    I.show()
    del I
    
    
def Mandelbrot_couleur(q):
    
    I=Image.new("RGB",(q,q))
    M=m.load(open("Mandelbrot"+str(q),"rb"))
    for i in range (q):
        for j in range (int(q/2)+1):
            e=M[i][j][2]
            if e==200 :
                I.putpixel((i,j),(30,30,30))
                I.putpixel((i,q-j-1),(30,30,30))
            else :   
                H=(e/50)
                r,g,b=hls_to_rgb(H,0.5,1)            
             
                R=int(225*r)
                G=int(225*g)
                B=int(225*b)
                I.putpixel((i,j),(R,G,B))
                I.putpixel((i,q-j-1),(R,G,B))
            
    I.save("Mandelbrot_couleur,q="+str(q))
    I.show()
    del I
               
               
               
def Mandelbrot_harmonique(f,nb,q):
      "f est la fréquence du signal"
      "nb désigne le nombre de terme de la somme du coefficient de fourrier"
      "retourne Mandelbrot après stimulation avec signal de fréquence f"
      
      I=Image.new("RGB",(q,q))
      M=m.load(open("Mandelbrot"+str(q),"rb"))
      for i in range (q):
         for j in range (int(q/2)+1):
             if M[i][j][0]!=complex(0,0) :
                 e1=coeff_fourrier(f,M[i][j][0],nb)
                 R1=int(225*(e1/nb)**2)
                 G1=int(225*(e1/nb)**2)
                 B1=int(225*(e1/nb))
                 I.putpixel((i,j),(R1,G1,B1))
                 
                 e2=coeff_fourrier(f,M[i][j][0].conjugate(),nb)
                 R2=int(225*(e2/nb)**2)
                 G2=int(225*(e2/nb)**2)
                 B2=int(225*(e2/nb))
                 I.putpixel((i,q-j-1),(R2,G2,B2))
       
             else:
                 I.putpixel((i,j),(40,20,0))
                 I.putpixel((i,q-j-1),(40,20,0))
                 
                 
      I.save("Mandelbrot_harmonique_f="+str(f)+"_q="+str(q)+".png")
      I.show()
      del I    

Mandelbrot_classique(400)   
