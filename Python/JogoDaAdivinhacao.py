from random import randint
from time import sleep
from os import system

def cabecalho():
    print('=' * 25)
    print('JOGO DA ADIVINHAÇÃO v1.0')
    print('=' * 25)
    print('\n\n')

cabecalho()
numero_user = int(input('Digite um número entre 1 e 5: '))
numero_maquina = randint(1, 5)

system('cls')

cabecalho()
print('PENSANDO...')
sleep(1)

system('cls')

cabecalho()

if numero_user == numero_maquina:
    print(f'ACERTOU! ERA O NÚMERO {numero_maquina}')
else:
    print(f'ERROU! VOCÊ INSERIU O NÚMERO {numero_user} E ERA O NÚMERO {numero_maquina}')

input()