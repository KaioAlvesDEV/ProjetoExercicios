import os
def cabecalho():
    print('||||||||||||||||||||')
    print('|DATA DE NASCIMENTO|')
    print('|           by kaio|')
    print('||||||||||||||||||||\n\n')

cabecalho()
data_nasc = input('INSIRA SUA DATA DE NASCIMENTO SEPARADA POR ESPAÇO EM BRANCO: ').replace(' ', '/')
os.system('cls')

cabecalho()
print(f'Você nasceu na data {data_nasc}')
input()
