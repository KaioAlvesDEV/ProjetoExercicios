numero = int(input('Digite um número de 0 até 9999: '))
print(f'PRIMEIRO DÍGITO: {numero // 1000 % 10}\nSEGUNDO: {numero // 100 % 10}\nTERCEIRO: {numero // 10 % 10}\nQUARTO: {numero // 1 % 10}')
input()