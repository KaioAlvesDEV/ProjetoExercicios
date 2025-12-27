from random import randint

lista_temp = []
jogos_mega_sena = []

qtd_jogos = int(input('Quantos jogos da Mega Sena você quer gerar? '))
qtd_digitos_qtd_jogos = len(str(qtd_jogos))

for jogo in range(qtd_jogos):
    for n in range(6):
        numero = randint(1, 60)
        while numero in lista_temp:
            numero = randint(1, 60)
        lista_temp.append(numero)
    lista_temp.sort()
    jogos_mega_sena.append(lista_temp[:])
    lista_temp.clear()

print('\n===== MEGA SENA =====')
for i, jogo in enumerate(jogos_mega_sena, 1):
    print(f'JOGO {i}:', end=' ' * (qtd_digitos_qtd_jogos - len(str(i)) + 1))
    for numero in jogo:
        print(f'{numero:02}', end=', ' if numero != jogo[-1] else '\n')
