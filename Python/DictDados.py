from random import randint
from time import sleep

jogadores = []

for i in range(1, 5):
    jogadores.append({'Jogador': f'Jogador {i}', 'Dado': randint(1, 6)})
    sleep(1)
    print(f'{jogadores[-1]["Jogador"]} jogou o dado e tirou {jogadores[-1]["Dado"]}')

jogadores_ordenados = sorted(
    jogadores,
    key=lambda jogador: jogador['Dado'],
    reverse=True
)
print('\n=== RANKING DOS JOGADORES ===')
for i, jogador in enumerate(jogadores_ordenados, 1):
    print(f'  {i}º lugar: {jogador["Jogador"]} com {jogador["Dado"]}.')
