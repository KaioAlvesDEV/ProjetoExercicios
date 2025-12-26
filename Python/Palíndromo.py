frase = input('Digite uma frase: ').strip().replace(' ', '').upper()

if len(set(frase)) == 1:
    print('É palíndromo')
else:
    inverso = ''
    for i in range(len(frase) - 1, -1, -1):
        inverso += frase[i]
        #print(inverso)

    if inverso == frase:
        print(f'A frase {frase} é palíndroma')
    else:
        print(f'{frase} Não é palíndroma pois seu inverso é {inverso}')
