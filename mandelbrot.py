
from PIL import Image
import threading
size = 300
iteration = 100
im = Image.new('RGB', (size, size))

class calcThread1(threading.Thread):
    def __init__(self):
        self.im = Image.new('RGB', (int(size/2), size))
        threading.Thread.__init__(self)

    def run(self):    
        for j in range(int(size/2)):
            for i in range(int(size/2)):

                x=float(i/size)*3-2.3
                y=float(j/size)*3-1.5
                c = complex(x,y)
                val = dive(c,iteration)
                Pval = int(val*255/iteration)
                self.im.putpixel((i, j), (Pval,Pval,Pval))
                self.im.putpixel((i,size- j), (Pval,Pval,Pval))
        print("done")
        self.im.show()

class calcThread2(threading.Thread):
    def __init__(self):
        self.im = Image.new('RGB', (int(size/2),size))
        threading.Thread.__init__(self)
        print("2 init")



    def run(self):    
        for j in range(int(size/2)):
            for i in range(int(size/2)):

                x=float(i/size)*3-2.3+1.5
                y=float(j/size)*3 - 1.5
                c = complex(x,y)
                val = dive(c,iteration)
                Pval = int(val*255/iteration)
                self.im.putpixel((i, j), (Pval,Pval,Pval))
                self.im.putpixel((i,size-j), (Pval,Pval,Pval))
        print("done")
        self.im.show()

def dive(c,P):
    "P : nombre d'itérations pour voir si la suite est bornée"
    
    if abs(1-(1-4*c)**0.5)<1 :
        return 0
    if abs(c+1)<0.24 :
        return 0
    compteur=0
    z=c   
    while abs(z)<2:
        z=z*z+c
        compteur+=1
        if (compteur == P):
            return 0
    return compteur


thread1 = calcThread1()
thread2 = calcThread2()
print("yup")
# Start new Threads
thread1.start()
thread2.start()