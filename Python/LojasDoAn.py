print(f'{'LOJAS DO AN':=^40}\n')
print('FORMAS DE PAGAMENTO\n[ 1 ] À vista dinheiro/cheque\n[ 2 ] À vista cartão')
print('[ 3 ] 2x no cartão\n[ 4 ] 3x no cartão')

juros_por_opcao = [-0.1, -0.05, 0, 0.2]
qtd_parcelas = 1

opcao_usuario = int(input('Escolha uma opção: '))
while opcao_usuario > 4 or opcao_usuario < 1:
    opcao_usuario = int(input('Opção Inválida! Escolha novamente: '))
juros = juros_por_opcao[opcao_usuario - 1]

preco_formal = float(input('Qual o preço das compras? '))
preco_final = preco_formal + preco_formal * juros

if opcao_usuario == 4:
    qtd_parcelas = int(input('Quantas parcelas? '))
    while qtd_parcelas < 3:
        qtd_parcelas = int(input('NÃO PODE SER MENOR QUE 3! Quantas parcelas? '))
elif opcao_usuario == 3:
    qtd_parcelas = 2

preco_mensal = preco_final / qtd_parcelas

print(f'São {qtd_parcelas} parcelas de {preco_mensal:.2f} reais ao mês! Preço total de R${preco_final:.2f}')

input()
