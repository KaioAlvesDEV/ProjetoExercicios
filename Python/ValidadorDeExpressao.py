try:
    permitidos = '0123456789()/+-*. '
    expressao = input('Digite uma expressão numérica: ')
    validador = 0
    for letra in expressao:
        if letra == '(':
            validador += 1
        if letra == ')':
            if validador == 0:
                validador = -1
                break
            validador -= 1

    if validador == 0:
        if all(char in permitidos for char in expressao):
            try:
                resultado = eval(expressao)
                print(f'O resultado da expressão é {resultado}')
            except SyntaxError:
                print('Expressão inválida')
            except ZeroDivisionError:
                print('Impossível divisão por zero')
        else:
            print('Expressão inválida')
    else:
        print(f'Expressão inválida')
    print('FINALIZADO')
    input()
except KeyboardInterrupt:
    print('\nFINALIZADO')
input()
