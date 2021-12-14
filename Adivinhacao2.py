import random


def jogar():
    print('*********************************')
    print('*\t\tJogo de advinhação\t\t*')
    print('*********************************')

    dif, pontos = definir_dificuldade_pontos()
    chave = definir_numero(dif)
    vida = quantidade_tentativas(dif)

    for rodada in range(0, vida):
        print(f'Rodada {rodada+1} de {vida}')
        chute = int(input('Insira seu chute: '))

        menor = chave > chute > 0
        maior = chute > chave > 0
        igual = chute == chave

        if igual:
            print('Você acertou, parabéns!')
            pontos += chute
            break
        elif maior:
            print('Você errou :(')
            print('Tente um número menor')
            pontos += -chute
        elif menor:
            print('Você errou :(')
            print('Tente um número maior')
            pontos += -chute
        else:
            print('Seu chute não pode ser menor que 0!')

    print(f'total de pontos: {pontos}!')


def definir_dificuldade_pontos():
    print('(1) Fácil\t(2) Médio\t(3) Díficil')
    escolha = input('Insira a dificuldade desejada: ')

    if escolha == '1':
        print('Você escolheu Fácil')
        print('Seu número está entre 0 e 25 e você tem 5 tentativas!')
        pontos = 25

    elif escolha == '2':
        print('Você escolheu Médio')
        print('Seu número está entre 0 e 50 e você tem 4 tentativas!')
        pontos = 50

    else:
        print('Você escolheu Díficil')
        print('Seu número está entre 0 e 100 e você tem 3 tentativas!')
        pontos = 100
    return escolha, pontos


def definir_numero(dif):
    if dif == '1':
        num = random.randrange((0, 26))
    elif dif == '2':
        num = random.randrange(0, 51)
    else:
        num = random.randrange(0, 101)
    return num


def quantidade_tentativas(dif):
    if dif == '1':
        vida = 5
    elif dif == '2':
        vida = 4
    else:
        vida = 3
    return vida


if __name__ == '__main__':
    jogar()
