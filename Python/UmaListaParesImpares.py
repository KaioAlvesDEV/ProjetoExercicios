# Criando uma lista com duas sublistas: uma para pares e outra para ímpares
pares_impares = [[], []]

# Coletando 7 números do usuário
for i in range(1, 8):
    
    num = int(input(f'Digite o {i}º valor: '))

    # Classificando números em pares e ímpares
    if num % 2 == 0:
        pares_impares[0].append(num)
    else:
        pares_impares[1].append(num)

pares_impares[0].sort()
pares_impares[1].sort()

# Exibindo os números pares e ímpares
print('Números pares digitados: ', end=': ')
for par in pares_impares[0]:
    print(par, end='')
    if par != pares_impares[0][-1]:
        print(',', end=' ')

print('\nNúmeros ímpares digitados: ', end=': ')
for impar in pares_impares[1]:
    print(impar, end='')
    if impar != pares_impares[1][-1]:
        print(',', end=' ')
