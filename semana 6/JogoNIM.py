def computador_escolhe_jogada(n,m):

    computador_escolhe_jogada = 1
    while computador_escolhe_jogada != m :
        if (n - computador_escolhe_jogada) % (m+1) == 0:
            return computador_escolhe_jogada 
        else: 
            computador_escolhe_jogada = computador_escolhe_jogada + 1
    return computador_escolhe_jogada

def usuario_escolhe_jogada(n,m):

    jogadaValida = False
    while not jogadaValida:
        usuario_escolhe_jogada= int(input("Quantas peças você vai tirar?"))
        if usuario_escolhe_jogada > m or usuario_escolhe_jogada < 1:
            print("\nOops! Jogada inválida! Tente de novo.")
        else:
            jogadaValida = True
    return usuario_escolhe_jogada


# partida

# n = numero de pecas totais no jogo
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
            ComputadorRemove = computador_escolhe_jogada(n,m)
            n = n - ComputadorRemove
            if ComputadorRemove == 1:
                print("\n O computador tirou uma peça ")
            else:
                print("\n O computador tirou",ComputadorRemove,"peças")
            VezDoPc = False
        else:
            JogadorRemove = usuario_escolhe_jogada(n,m)
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
    print("\nFim do jogo! O computador ganhou!")


# campeonato
def campeonato():
    contador = 3
    while contador > 0:
        partida()
        contador -= 1
    print("\nFim do jogo! O computador ganhou!")
    print("\n**** Final do campeonato! ****")
    print("\nPlacar: Você 0 X 3 Computador")


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