from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Insira o seu ano de nascimento: '))
idade = ano_atual - ano_nascimento
tiers_natacao = ['MIRIM', 'INFANTIL', 'JÚNIOR', 'SÊNIOR', 'MASTER']
idade_tier = [9, 14, 19, 25]

print('CATEGORIA', end=' ')

if idade <= idade_tier[0]:
    print(f'{tiers_natacao[0]}')
elif idade <= idade_tier[1]:
    print(f'{tiers_natacao[1]}')
elif idade <= idade_tier[2]:
    print(f'{tiers_natacao[2]}')
elif idade <= idade_tier[3]:
    print(f'{tiers_natacao[3]}')
else:
    print(f'{tiers_natacao[4]}')

input()
