nums = []
resp = 'SIM'

while resp not in ('N', 'NÃO', 'NAO'):

    numero_usuario = int(input('Digite um número: '))
    if numero_usuario in nums:
        print('Valor já está na lista!')
    else:
        nums.append(numero_usuario)

    while True:

        resp = input('Quer continuar? [S/N/SIM/NAO/NÃO]: ').upper().strip()
        if resp in ('S', 'N', 'SIM', 'NAO', 'NÃO'): break

nums.sort()
print(f'OS NÚMEROS DIGITADOS DO MENOR PARA O MAIOR FORAM: {nums}')
