soma_numeros = 0
qtd_numeros_digitados = 0
parar = False

while not parar:
    soma_numeros += float(input('Insira um número para ver a média: '))
    qtd_numeros_digitados += 1
    parar = bool(input('Quer parar? (ENTER para continuar e qualquer coisa para parar)'))

media = soma_numeros/qtd_numeros_digitados
print(f'MÉDIA: {media:>5}')
input()