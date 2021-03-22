def jogadaPC(n,m):

    jogadaPC = 1
    while jogadaPC != m :
        if (n - jogadaPC) % (m+1) == 0:
            return jogadaPC 
        else: 
            jogadaPC = jogadaPC + 1
    return jogadaPC

def jogadajogador(n,m):

    jogadaValida = False
    while not jogadaValida:
        jogadajogador= int(input("Quantas peças você vai tirar?"))
        if jogadajogador > m or jogadajogador < 1:
            print("\nOops! Jogada inválida! Tente de novo.")
        else:
            jogadaValida = True
    return jogadajogador


# partida

# # n = numero de pecas totais no jogo
# m = numero maximo de pecas jogadas por rodada

def partida():
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    VezDoPc = False
    if n % (m + 1) == 0:
        print("\nVoce começa!") 
    else:
        print("\nComputador começa!")
        VezDoPc = True
    while n > 0:
        if VezDoPc:
            ComputadorRemove = jogadaPC(n,m)
            n = n - ComputadorRemove
            if ComputadorRemove == 1:
                print("\n O computador tirou uma peça ")
            else:
                print("\n O computador tirou",ComputadorRemove,"peças")
            VezDoPc = False
        else:
            JogadorRemove = jogadajogador(n,m)
            n = n- JogadorRemove            
            if JogadorRemove == 1:
                print("\nVocê tirou uma peça")
            else:
                print("\nVocê tirou",JogadorRemove,"peças")
            VezDoPc = True
        if n == 1:
            print("\nAgora resta apenas uma peça no tabuleiro.")
        else: 
            print("\nAgora restam",n,"peças no tabuleiro.")


# campeonato
def campeonato():
    contador = 3
    while contador > 0:
        partida()
        contador -= 1


print("\nBem-vindo ao jogo do NIM! Escolha:\n")

print("1 - para jogar uma partida isolada")

tipoDePartida = int(input("2 - para jogar um campeonato "))

# partida 1 para partida
# partida 2 para campeonato

if tipoDePartida == 2:
    print("\nVoce escolheu um campeonato!\n")
    campeonato()
else:
    print("\nVoce escolheu uma partida isolada\n")
    partida()