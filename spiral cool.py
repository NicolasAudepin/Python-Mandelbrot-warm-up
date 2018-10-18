# -*- coding: utf-8 -*-
"""
Created on Sun May  8 13:53:42 2016

@author: AUDEPIN
"""

import cmath as c
import numpy as np
import matplotlib.pyplot as plt


def C2(n):
    l=[]
    for i in range (n+1):
        l.append(i**2)
    return l
    
def spy(L):
    Z=[0]
    for i in range (1,len(L)):
        d=L[i]-L[i-1]
        for j in range(1,d+1):
            z=c.rect(i+(j/d),np.pi*2*j/d)
            Z.append(z)
    return Z
    
def grax(Z):
    X=[]
    Y=[]
    for z in Z:
        X.append(z.real)
        Y.append(z.imag)
    plt.plot(X,Y,"x")  
    
def gra(Z):
    X=[]
    Y=[]
    for z in Z:
        X.append(z.real)
        Y.append(z.imag)
    plt.plot(X,Y,"o")  

def deux(n):
    Lp=Prim(n)
    Ld=[]
    for k in range (2,n+1):
        be=0
        for i in Lp:
            if k%i==0 and be==0:
                be=1
            elif k%i==0 and be==1:
                be=2
        if be==1 :
            Ld.append(k)
    return Lp
   
def Prim(n):
    Lp=[2]
    for k in range (2,n+1):
        be=0
        for i in Lp:
            if k%i==0:
                be=1  
        if be==0 :
            Lp.append(k)
    return Lp
    
def style(n):
    Z=spy(C2(n))
    Zp=[]
    Pr=Prim(n**2)
    for p in Pr:
        Zp.append(Z[p])
    Zd=[]    
    Pd=deux(n**2)
    for d in Pd:
        Zd.append(Z[d])
    grax(Z)
    gra(Zp)
    gra(Zd)