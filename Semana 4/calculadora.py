quant = int(input("Digite quantos numeros deverao ser calculados: "))
soma=0
valor=1
if quant != 0:
    while (quant != 0):
        valor = int(input("Insira Numero: "))
        soma = soma + valor
        quant = quant - 1
else:
    print("Numero negativo Invalido ")
print("Resultado da soma: ",soma)