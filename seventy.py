def proximoMultiplo(num):
    return num + (4 - (num % 4))


def perdedor1(pontos):
    print("\n\nVocê Perdeu!!")
    print(f"Você fez {pontos} pontos.")
    print("Mais sorte na próxima vez!")
    exit(0)


def verificar(xyz):
    i = 1
    while i < len(xyz):
        if xyz[i] - xyz[i - 1] != 1:
            return False
        i = i + 1
    return True


def comecar1():
    xyz = []
    ultimo = 0
    i, j = 1, 1  # Inicializando i e j
    pontos = 0  # Inicialização dos pontos
    while True:
        print("Aperte 'F' para ter a primeira chance.")
        print("Aperte 'S' para ter a segunda chance.")
        chance = input('> ')

        if chance == "F":
            while i <= 3:
                if ultimo == 20:
                    perdedor1()
                print("\nSeu Turno.")
                print("\nQuantos números você deseja inserir?")
                inp = int(input('> '))
                if 0 < inp <= 3:
                    comp = 4 - inp
                    print("Agora digite os valores")
                    while i <= inp:
                        a = int(input('> '))
                        xyz.append(a)
                        i = i + 1
                        ultimo = xyz[-1]
                        if verificar(xyz) == True:
                            while j <= comp:
                                xyz.append(ultimo + j)
                                j = j + 1
                            print("A ordem das entradas após a vez do computador é: ")
                            print(xyz)
                            ultimo = xyz[-1]
                    else:
                        print("\nVocê não inseriu números inteiros consecutivos.")
                        perdedor1(pontos)
                else:
                    print("Entrada errada. Você está desqualificado do jogo")
                    perdedor1()

        elif chance == "S":
            comp = 1
            ultimo = 0
            while ultimo < 20:
                j = 1
                while j <= comp:
                    xyz.append(ultimo + j)
                    j = j + 1
                print("A ordem das entradas após a vez do computador é: ")
                print(xyz)
                if xyz[-1] == 20:
                    perdedor1()
                else:
                    print("\nSeu Turno")
                    print("\nQuantos números você deseja inserir?")
                    inp = int(input('> '))
                    i = 1
                    print("Insira seus valores")
                    while i <= inp:
                        xyz.append(int(input('> ')))
                        i = i + 1
                        pontos += 1  # Incrementando pontos
                    ultimo = xyz[-1]
                    if verificar(xyz) == True:
                        proximo = proximoMultiplo(ultimo)
                        comp = proximo - ultimo  # Correção no cálculo de 'comp'
                        if comp == 4:
                            comp = 3
                    else:
                        print("\nVocê não inseriu números inteiros consecutivos.")
                        perdedor1(pontos)  # Passando pontos para a função perdedor1
                print("\nPARABENSSSSS!!!")
                print(f"\nVOCÊ VENCEU com {pontos} pontos!!")
                exit(0)
            else:
                print("Escolha errada")


jogo = True
while jogo == True:
    print("O jogador 2 é o computador.")
    print("Você quer jogar o jogo de 21 números? (Sim / Não)")
    ans = input('> ')
    if ans.lower() == 'sim':
        comecar1()
    else:
        print("Você quer sair do jogo? (sim / não)")
        nex = input('> ')
        if nex.lower() == "sim":
            print("Você está saindo do jogo...")
            exit(0)
        elif nex.lower() == "não":
            print("Continuando...")
        else:
            print("Escolha perigosa")
