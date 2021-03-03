a = int(input("Insira o valor de A: "))
b = int(input("Insira o valor de B: "))
c = int(input("Insira o valor de C: "))
delta=(b**2)-(4*a*c)
x1= (-b + (delta ** (1/2))) / (2*a)
x2= (-b - (delta ** (1/2))) / (2*a)
if delta < 0:
    print("esta equação não possui raízes reais")
if delta == 0:
    print("a raiz desta equação é",x1)
if delta > 0:
    if x1 < x2:
        print("as raízes da equação são",x1,"e",x2)
    else:
        print("as raízes da equação são",x2,"e",x1)