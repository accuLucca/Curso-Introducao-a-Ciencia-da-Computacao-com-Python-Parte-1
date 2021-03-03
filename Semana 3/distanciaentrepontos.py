x1 = float(input("Insira um numero coordenada x1: "))
y1 = float(input("Insira um numero coordenada y1: "))
x2 = float(input("Insira um numero coordenada x2: "))
y2 = float(input("Insira um numero coordenada y2: "))
import math
if (math.sqrt((x1 - x2)**2+(y1 - y2)**2)) >= 10:
    print("longe")
else:
    print("perto")