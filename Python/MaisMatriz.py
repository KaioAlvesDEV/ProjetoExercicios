matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Inicializando variáveis para cálculos
soma_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = 0

# Preenchendo a matriz com valores fornecidos pelo usuário
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para a posição ({l}, {c}): '))

        # Calculando soma dos pares
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]

        # Calculando soma da terceira coluna
        if c == 2:
            soma_terceira_coluna += matriz[l][c]

        # Encontrando o maior valor da segunda linha
        if l == 1:
            if c == 0 or matriz[l][c] > maior_valor_segunda_linha:
                maior_valor_segunda_linha = matriz[l][c]

# Exibindo a matriz formatada
print('Matriz Formatada:')
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:<3}]', end=' ')
    print()

# Exibindo os resultados calculados
print(f'A soma dos valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_valor_segunda_linha}')
