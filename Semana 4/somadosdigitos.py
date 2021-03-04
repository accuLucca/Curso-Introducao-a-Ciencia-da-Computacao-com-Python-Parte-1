n = int(input("Digite um número inteiro: "))
x = 0
while n > 9:
    x = x +(n % 10)
    n = n // 10
print(x+n)