from PIL import Image
size = 1000
iteration = 10
image = Image.new('RGB', (size, size))
image.show()



def dive(c,P):
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

    

for i in range(size):
    for j in range(size):
        
        c = complex(x,y)
        val = dive(c,iteration)
        print(val)
        image.putpixel((i, j), (val,val,val)
image.show()