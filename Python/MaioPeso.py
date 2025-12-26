maior_peso = 0
menor_peso = 0

for pessoa in range(0, 5):
    peso_atual = float(input(f'Qual o peso da pessoa número {pessoa + 1}? '))
    if peso_atual > maior_peso:
        maior_peso = peso_atual
    if pessoa == 0:
        menor_peso = maior_peso
    if peso_atual < menor_peso:
        menor_peso = peso_atual
print(f'MAIOR PESO: {maior_peso}\nMENOR PESO: {menor_peso}')
