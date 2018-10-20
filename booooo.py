from PIL import Image

print("ta mère visual studio")

x = 0
for i in range(20):
    x = x+1
    x=x*2
    print(x)

im = Image.new('RGB', (50, 50))
im.show()