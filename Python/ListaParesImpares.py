numeros = [int(input(f'Insira o {numero} número: ')) for numero in range(1, 6)]
numeros_pares = [numero for numero in numeros if numero % 2 == 0]
numeros_impares = [numero for numero in numeros if numero % 2 != 0]

print(f'Números pares inseridos foram {numeros_pares} e os ímpares foram {numeros_impares}')
