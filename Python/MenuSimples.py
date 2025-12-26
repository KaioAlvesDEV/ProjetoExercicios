from os import system

def mostrar_menu():
    print('-=' * 15)
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NÚMEROS')
    print('[ 5 ] SAIR')
    print('-=' * 15)

def selecionador_de_operacao(msg_personalizada_input) -> str:
    while True:
        try:
            opcao_num = int(input(msg_personalizada_input))
            while opcao_num < 1 or opcao_num > 5:
                opcao_num = int(input(f'ERRO!\n{msg_personalizada_input}'))
            break
        except ValueError:
            print('INSIRA UM VALOR VÁLIDO!')

    if opcao_num == 1:
        return 'SOMAR'
    elif opcao_num == 2:
        return 'MULTIPLICAR'
    elif opcao_num == 3:
        return 'MAIOR'
    elif opcao_num == 4:
        return 'NOVOS NÚMEROS'
    elif opcao_num == 5:
        return 'SAIR'
    return 'erro lógico'

def pedir_numero(msg_personalizada) -> float:
    while True:
        try:
            return float(input(msg_personalizada))
        except ValueError:
            print("INSIRA APENAS NÚMEROS VÁLIDOS!")

def somar(num, othernum) -> float:
    return num + othernum

opcao = ''
num1 = pedir_numero('INSIRA O PRIMEIRO NÚMERO: ')
num2 = pedir_numero('INSIRA O SEGUNDO NÚMERO: ')

while opcao != 'SAIR':
    mostrar_menu()
    opcao = selecionador_de_operacao('SELECIONE UMA OPÇÃO: ')
    if opcao == 'SOMAR':
        print(f'SOMA: {somar(num1, num2)}')
    if opcao == 'MULTIPLICAR':
        print(f'MULTIPLICAÇÃO: {multiplicar(num1, num2)}')
