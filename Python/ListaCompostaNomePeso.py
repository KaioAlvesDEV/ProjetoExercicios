pessoas = []

# Loop para adicionar pessoas até o usuário decidir finalizar   
while True:
    finalizar = 'EMPTY'
    # Solicitar nome e peso da pessoa
    nome_pessoa = input('Digite o nome da pessoa: ')
    peso_pessoa = float(input('Digite o peso da pessoa (kg): '))
    pessoas.append([nome_pessoa, peso_pessoa])

    # Perguntar se o usuário deseja finalizar
    while finalizar not in ('S', 'N', 'SIM', 'NÃO'):
        finalizar = input('Deseja finalizar? (S/N): ').upper()
    if finalizar in ('S', 'SIM'):
        break

# Exibir a lista de pessoas cadastradas
print('Lista de pessoas cadastradas:\nNome       Peso')
for pessoa in pessoas:
    print(f'{pessoa[0]:<11}{pessoa[1]:.2f} kg')
