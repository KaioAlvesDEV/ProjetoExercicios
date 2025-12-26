palavras = ('CASA', 'VERME', 'CORTINA', 'SAPATO', 'GUANABARA')

for palavra in palavras:
    print(f'NA PALAVRA {palavra} TEMOS AS VOGAIS ', end='')
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')
    print('\n')
