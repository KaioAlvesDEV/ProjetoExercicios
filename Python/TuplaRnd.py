from random import randint

numeros = tuple(randint(0, 100) for _ in range(10))

print('NÚMEROS GERADOS: ', end='')
for i, numero in enumerate(numeros):
    print(numero, end='')
    if i != 9:
        print(end=', ')
print(f'\nMAIOR: {max(numeros)}')
print(f'MENOR: {min(numeros)}')