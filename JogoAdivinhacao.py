import random


def jogar():
    print('\tJogo de advinhação')
    print('**********************************')
    print('\t Dificuldades: \nFácil\tMédio\tDifícil')
    escolha = input('Defina a dificuldade: ')
    print('**********************************')
    escolha = escolha.lower()

    facil = escolha == 'fácil'
    medio = escolha == 'médio'
    dif = escolha == 'dificíl'

    if facil:
        x = 26
        pontos = 25
        print('Seu número está entre 0 e 25')
    elif medio:
        x = 51
        pontos = 50
        print('Seu número está entre 0 e 50')
    else:
        x = 101
        pontos = 100
        print('Seu número está entre 0 e 100')

    correto = random.randrange(0, x)
    print(correto)
    print('Pontos iniciais: ', pontos)
    print('**********************************')

    for rodada in range(0, 3):
        print('Tentativa {} de {}'.format(rodada + 1, 3))

        chute = input('Digite seu chute: ')
        chute = int(chute)
        if chute < 0 or chute > x:
            print(f'O chute deve ser entre 0 e {x}!')
            continue

        acertou = chute == correto
        menor = chute < correto
        maior = chute > correto

        if acertou:
            print('Você acertou!\n')
            pontos = pontos + chute
            break
        else:
            if menor:
                print('Tente um número maior\n')
            elif maior:
                print('Tente um número menor\n')
            pontos = pontos - chute

    print(f'** Você fez {pontos} pontos! **')
    print('**********************************')
    print('\tFim de jogo!')


if __name__ == '__main__':
    jogar()
