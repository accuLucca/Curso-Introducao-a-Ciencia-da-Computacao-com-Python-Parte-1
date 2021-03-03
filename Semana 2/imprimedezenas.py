num=int(input("Insira um numero inteiro: "))
unidade=num%10
unidade=(num-unidade)/10
dezena=unidade%10
print("O dígito das dezenas é",int(dezena))