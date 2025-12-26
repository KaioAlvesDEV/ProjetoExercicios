soma_total = 0.0
nums_inseridos = 0
resposta = 'SIM'

while resposta in ['S','SIM']:
    num_atual = float(input('INSIRA UM NÚMERO: '))
    soma_total += num_atual
    nums_inseridos += 1

    if nums_inseridos == 1:
        menor = maior = num_atual
    else:
        if num_atual > maior:
            maior = num_atual
        if num_atual < menor:
            menor = num_atual

    resposta = str(input('CONTINUAR? [S/N]: ')).upper()
    while resposta not in ['S', 'SIM', 'N', 'NÃO', 'NAO']:
        resposta = input('INVÁLIDO! CONTINUAR? [S/SIM/N/NÃO/NAO]: ')

media = soma_total / nums_inseridos
print(f'''MÉDIA TOTAL DE {media:.2f}
MAIOR NÚMERO FOI {maior}
MENOR NÚMERO FOI {menor}''')
