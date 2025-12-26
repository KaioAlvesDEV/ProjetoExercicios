idade_tot = 0
homem_mais_velho_idade = 0
homem_mais_velho_nome = 'Não existem homens no grupo'
mulheres_mais_de_vinte_anos = 0

for pessoas in range(0, 4):
    print(f'{f'PESSOA {pessoas + 1}':=^25}')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    idade_tot += idade

    if idade > homem_mais_velho_idade and sexo == 'M':
        homem_mais_velho_idade = idade
        homem_mais_velho_nome = nome

    if idade > 20 and sexo == 'F':
        mulheres_mais_de_vinte_anos += 1

media_idade = idade_tot / 4

print(f'MÉDIA DA IDADE: {media_idade:.2f}\nHOMEM MAIS VELHO: {homem_mais_velho_nome}\nMULHERES COM MAIS DE 20 ANOS: {mulheres_mais_de_vinte_anos}')
