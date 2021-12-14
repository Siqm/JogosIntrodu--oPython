import Jogoforca
import Adivinhacao2


def escolhe_jogo():
    print('****************************')
    print('*\t   Escolha o Jogo\t   *')
    print('****************************')

    print('(1) - Adivinhação\t(2) - Forca')
    jogo = int(input('Qual jogo quer jogar: '))

    if jogo == 1:
        print('Iniciando jogo de Adivinhação!')
        Adivinhacao2.jogar()
    else:
        print('Iniciando jogo de Forca!')
        Jogoforca.jogar()


if __name__ == '__main__':
    escolhe_jogo()
