import math
a=int(input("Insira o valor de A: "))
b=int(input("Insira o valor de B: "))
c=int(input("Insira o valor de C: "))
delta=(b**2)-(4*a*c)
if delta < 0:
    print("Valor negativo nao pode!!")
else:
    delta=math.sqrt(delta)
    x1=(-b+delta)/(2*a)
    x2=(-b-delta)/(2*a)
    print("Valor de X+: ",x1,"Valor de X-: ",x2)