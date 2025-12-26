from os import system
from time import sleep

segundos_fogos = int(input('Quantos segundos até soltar os fogos? '))

for segs in range(segundos_fogos, 0, -1):
    print(f'\033[93mSegundos restantes: {segs:>10}', flush=True)
    sleep(1)
    system('cls')

print('\033[92mFOGOS SOLTADOS!')

input()
