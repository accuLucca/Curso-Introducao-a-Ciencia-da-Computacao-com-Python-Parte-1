numero= num = int(input("Insira um numero: "))
anterior = num % 10
num = num // 10
adjacente = False
posterior = True

while num > 0 and not adjacente:
    atual = num % 10
    if atual == anterior:
        adjacente = True
    else:
        posterior = posterior + 1
    anterior = atual
    num = num //10
if adjacente:
    print(numero,"Tem dois digitos",atual,"adjacentes")
else:
    print(numero,"nao tem digitos iguais adjancentes")