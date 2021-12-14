import random


def jogar():
    palavra_secreta = define_palavra()
    pl_resp = define_palavraResposta(palavra_secreta)

    erro = 0
    enforcou = False
    acertou = False

    print('****************************')
    print('*\tJogo da forca\t*')
    print('****************************\n')
    print(pl_resp)

    while not enforcou and not acertou:
        chute = input('Qual a letra: ').lower().strip()

        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, chute, pl_resp)

        else:
            erro = conta_erro(erro)

        enforcou = erro == 7
        acertou = '_' not in pl_resp
        print(pl_resp, '\n')

    fim_de_jogo(acertou, palavra_secreta)

    print('\tFim de jogo!')


def define_palavra():
    with open('palavras.txt') as arquivo:
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
        arquivo.close()

    num = random.randrange(0, len(palavras))
    palavra_secreta = palavras[num].lower()
    return palavra_secreta


def define_palavraResposta(palavra):
    return ['_' for letra in palavra]


def marca_chute_correto(palavra, chute, p_resp):
    i = 0
    for letra in palavra:
        if chute == letra:
            p_resp[i] = letra
        i += 1


def fim_de_jogo(acertou, palavra_secreta):
    if acertou:
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

    else:
        print("Puxa, você foi enforcado!")
        print(f"A palavra era {palavra_secreta.upper()}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")


def conta_erro(erro):
    erro += 1
    print(f'Você errou, restam {7 - erro} tentativas')
    print("  _______     ")
    print(" |/      |    ")

    if erro == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erro == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erro == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erro == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erro == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erro == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erro == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    return erro


if __name__ == '__main__':
    jogar()
