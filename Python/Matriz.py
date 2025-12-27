matriz = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]

# Preenchendo a matriz com letras fornecidas pelo usuário
for c in range(3):
    for l in range(3):
        matriz[c][l] = input(f'Digite uma letra para a posição ({c}, {l}): ')[0]

# Exibindo a matriz preenchida
for c in range(3):
    for l in range(3):
        print(f'{matriz[c][l]}', end=' ')
    print()
