valor_casa = float(input('Qual o valor da casa? '))
anos_parcelamento = int(input('Por quantos anos vai parcelar? '))
salario = float(input('Qual o seu salário? '))
valor_parcela_mensal = valor_casa / (anos_parcelamento * 12)

if salario * 0.3 < valor_parcela_mensal:
    print(f'Empréstimo negado! Você precisa ganhar pelo menos R${(valor_parcela_mensal / 0.3):.2f}')
else:
    print(f'Valor por parcela mensal: R${valor_parcela_mensal:.2f}')

input()
