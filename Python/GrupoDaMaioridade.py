from datetime import datetime

menores_idade = 0
maiores_idade = 0
ano_atual = datetime.now().year

for pessoa in range(0, 7):
    ano_nasc = int(input(f'Qual o ano de nascimento {pessoa + 1}nd pessoa? '))
    idade = ano_atual - ano_nasc
    if idade >= 0:
        if idade < 18:
            menores_idade += 1
        else:
            maiores_idade += 1

print(f'{maiores_idade} maiores de idade e {menores_idade} menores de idade')
