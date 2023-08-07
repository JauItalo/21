def proximoMultiplo(num):
    if num >= 4:
        proximo = num + (4 - (num %4))
    else:
        proximo = 4
    return proximo

def perdedor1():
    print("\n\n Você Perdeu!!")
    print("Mais sorte na proxima vez!")
    exit(0)

def verificar(xyz):
    i = 1
    while i < len(xyz):
        if (xyz[i]-xyz[i-1])!= 1:
            return False
        i = i + 1
    return True

def comecar1():
    xyz = []
    ultimo = 0
    while True:
        print("Aperte 'F' para ter a primeira chance.")
        print("Aperte 'S' para ter a segunda chance.")
        chance = input('>')

        if chance == "F":
            while True:
                if ultimo == 20:
                    perdedor1()
                else:
                    print("\nSeu Turno.")
                    print("\nQuantos números você deseja inserir?")
                    inp = int(input('> '))
                    if inp > 0 and inp <= 3:
                        comp = 4 - inp
                    else:
                        print("Entrada errada. Você está desqualificado do jogo")
                        perdedor1()
                        i, j = 1, 1
            print("Agora digite os valores")
            while i <= inp:
                    a = input('> ')
                    a = int(a)
                    xyz.append(a)
                    i = i + 1
                    ultimo = xyz[-1]    
                    if verificar(xyz) == True:
                        if ultimo == 21:
                            perdedor1()
                        else:
                            while j <= comp:
                                xyz.append(ultimo + j)
                                j = j + 1
                                print("A ordem das entradas após a vez do computador é: ")
                                print(xyz)
                                ultimo = xyz[-1]
            else:
                print("\nVocê não inseriu números inteiros consecutivos.")
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
                    inp = input('> ')
                    inp = int(inp)
                    i = 1
                    print("Insira seus valores")
                    while i <= inp:
                        xyz.append(int(input('> ')))
                        i = i + 1
                    ultimo = xyz[-1]
                    if verificar(xyz) == True:
                        proximo = proximoMultiplo(ultimo)
                        comp = ultimo - ultimo
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp
                    else:
                        print("\nVocê não inseriu números inteiros consecutivos.")
                        perdedor1()
            print("\nPARABENSSSSS!!!")
            print("\nVOCÊ VENCEU!!")
            exit(0)
        else:
            print("Escolha errada")

jogo = True
while jogo == True:
    print("O jogador 2 é o computador.")
    print("Você quer jogar o jogo de 21 números? (Sim não)")
    ans = input('> ')
    if ans == 'Yes':
        comecar1()
    else:
        print("Você quer sair do jogo? (sim / não)")
        nex = input('> ')
        if nex == "yes":
            print("Você esta saindo do jogo...")
            exit(0)
        elif nex == "no":
            print("Continuando...")
        else:
            print("Esolha perigosa")