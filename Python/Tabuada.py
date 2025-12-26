numero_tabuada = int(input('Digite um número para ver sua tabuada: '))
for i in range(1, 11):
    print(f'{numero_tabuada} X {i} = {numero_tabuada * i:>5}')
input()