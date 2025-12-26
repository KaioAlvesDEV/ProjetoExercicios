from random import randint
from time import sleep
from os import system

def cabecalho_estatico():
    system('cls')
    print('', '\033[94m|' * 31)
    print(f' {'Jogo Da Adivinhação 2':|^31}')
    print('', '|' * 31)
    print('\n')

def cabecalho_animado(mensagem_personalizada):
    animacao = ['\\', '|', '/', '|', '\\', '|', '/', '|']

    for frame in range(0, len(animacao)):
        system('cls')
        print(f' \033[94m{animacao[frame] * 31}', flush = True)
        print(f' {'Jogo Da Adivinhação 2':{animacao[frame]}^31}', flush = True)
        print('', animacao[frame] * 31, flush = True)
        print(f'\n{mensagem_personalizada}')
        sleep(0.25)

numero_maquina = randint(1, 10)
numero_usuario = 0
numeros_digitados = []
tentativas = 0

cabecalho_animado('\033[93m By Kaio')

while numero_usuario != numero_maquina:
    cabecalho_estatico()
    try:
        numero_usuario = int(input('\033[93m Insira um palpite (1 até 10): '))

        while numero_usuario < 1 or numero_usuario > 10:
            cabecalho_animado('\033[91m INSIRA UM NÚMERO ENTRE 1 E 10!')
            cabecalho_estatico()
            numero_usuario = int(input('\033[93m Insira um palpite (1 até 10): '))

        while numero_usuario in numeros_digitados:
            cabecalho_animado('\033[91m INSIRA UM NÚMERO AINDA NÃO DIGITADO!')
            cabecalho_estatico()
            numero_usuario = int(input('\033[93m Insira um palpite (1 até 10): '))

        numeros_digitados.append(numero_usuario)

        cabecalho_animado('\033[93m PENSANDO...')

        if numero_usuario == numero_maquina:
            pontuacao = 1000 - tentativas * 100
            if pontuacao == 1000:
                mensagem_final = '\033[92m PONTUAÇÃO MÁXIMA!'
            elif 900 >= pontuacao > 700:
                mensagem_final = '\033[92m VOCÊ TÁ VOANDO!'
            elif 700 >= pontuacao > 500:
                mensagem_final = '\033[93m NADA DEMAIS'
            elif pontuacao == 500:
                mensagem_final = '\033[93m METADINHA'
            elif 400 >= pontuacao > 200:
                mensagem_final = '\033[91m TEM QUE MELHORAR'
            elif pontuacao == 200:
                mensagem_final = '\033[91m TÁ AZARENTO EIN'
            else:
                mensagem_final = '\033[91m EITA...'

            cabecalho_animado(f'\033[92m ACERTOU! {tentativas + 1} TENTATIVA(S) NECESSÁRIAS: {pontuacao} PONTOS!\n{mensagem_final}')
            break
        else:
            tentativas += 1
            cabecalho_animado('\033[91m ERROU!')
    except ValueError:
        print('\033[91m POR FAVOR, INSIRA UM VALOR INTEIRO')
        sleep(1)
