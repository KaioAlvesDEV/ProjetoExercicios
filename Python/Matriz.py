matriz = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]

# Preenchendo a matriz com letras fornecidas pelo usuário
for l in range(3):
    for c in range(3):
        matriz[l][c] = input(f'Digite uma letra para a posição ({l}, {c}): ')[0]

# Exibindo a matriz preenchida
for l in range(3):
    for c in range(3):
        print(f'{matriz[l][c]}', end=' ')
    print()
