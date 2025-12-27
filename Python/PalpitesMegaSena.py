from random import randint
from time import sleep

# Inicializando listas para armazenar os números temporários e os jogos gerados
lista_temp = []
jogos_mega_sena = []

# Solicitando ao usuário a quantidade de jogos a serem gerados
qtd_jogos = int(input('Quantos jogos da Mega Sena você quer gerar? '))
qtd_digitos_qtd_jogos = len(str(qtd_jogos))

# Gerando os jogos da Mega Sena
for jogo in range(qtd_jogos):

    # Gerando 6 números únicos para cada jogo
    for n in range(6):

        numero = randint(1, 60)

        # Garantindo que os números sejam únicos dentro do jogo
        while numero in lista_temp:
            numero = randint(1, 60)
        lista_temp.append(numero)
    
    # Ordenando os números do jogo antes de adicionar à lista de jogos
    lista_temp.sort()
    jogos_mega_sena.append(lista_temp[:])
    lista_temp.clear()

# Exibindo os jogos gerados
print('\n', '=====' * 7, 'MEGA SENA', '=====' * 7)
for i, jogo in enumerate(jogos_mega_sena, 1):

    sleep(0.5)
    # Formatação para alinhar os números dos jogos
    print(f'JOGO {i}:', end=' ' * (qtd_digitos_qtd_jogos - len(str(i)) + 1))
    for numero in jogo:
        print(f'{numero:02}', end=', ' if numero != jogo[-1] else '\n')
