from os import system

def cabecalho():
    system('cls')
    print(' ╔═══════╗ by')
    print(' ║SOMADOR║ ka')
    print(' ╚═══════╝ io\n\n')

cabecalho()
num1 = int(input(' Insira o primeiro número : '))
input()

cabecalho()
num2 = int(input(' Insira o segundo número : '))
input()

cabecalho()
soma = num1 + num2
print(f' sA soma {num1} + {num2} resulta em {soma}!')
input()
