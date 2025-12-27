pessoas = [] # Lista para armazenar os dados das pessoas
pessoas_mais_pesadas_nomes = [] # Lista para nomes das pessoas mais pesadas
pessoas_mais_leves_nomes = [] # Lista para nomes das pessoas mais leves
maior_peso = menor_peso = 0.0 # Variáveis para armazenar maior e menor peso

# Loop para adicionar pessoas até o usuário decidir finalizar   
while True:

    finalizar = 'EMPTY'

    # Solicitar nome e peso da pessoa
    nome_pessoa = input('Digite o nome da pessoa: ')
    peso_pessoa = float(input('Digite o peso da pessoa (kg): '))
    pessoas.append([nome_pessoa, peso_pessoa])

    # Contar o número de pessoas cadastradas
    num_pessoas_cadastradas = len(pessoas)
    print(f'Pessoa cadastrada com sucesso! Total de pessoas cadastradas: {num_pessoas_cadastradas}')

    # Perguntar se o usuário deseja finalizar
    while finalizar not in ('S', 'N', 'SIM', 'NÃO'):
        finalizar = input('Deseja finalizar? (S/N): ').upper()
    if finalizar in ('S', 'SIM'):
        break

# Exibir a lista de pessoas cadastradas
print('Lista de pessoas cadastradas:\nNome       Peso')
for pessoa in pessoas:
    print(f'{pessoa[0]:<11}{pessoa[1]:.2f} kg')

# Determinar maior e menor peso
pessoas_mais_pesadas = []
pessoas_mais_leves = []

# Analisar os pesos para encontrar os mais pesados e mais leves
for i, pessoa in enumerate(pessoas):

    # Inicializar maior e menor peso na primeira iteração
    if i == 0:

        maior_peso = menor_peso = pessoa[1]
        pessoas_mais_pesadas.append(pessoa[0])
        pessoas_mais_leves.append(pessoa[0])

    else:

        # Comparar pesos para atualizar listas de mais pesados e mais leves
        if pessoa[1] >= maior_peso:

            if pessoa[1] > maior_peso: # Novo maior peso encontrado
                pessoas_mais_pesadas.clear()
                maior_peso = pessoa[1]

            pessoas_mais_pesadas.append(pessoa[0])

        if pessoa[1] <= menor_peso:

            if pessoa[1] < menor_peso: # Novo menor peso encontrado
                menor_peso = pessoa[1]
                pessoas_mais_leves.clear()

            pessoas_mais_leves.append(pessoa[0])

# Saída dos resultados
print('Número total de pessoas cadastradas:', num_pessoas_cadastradas)
print(f'Maior peso registrado: {pessoas_mais_pesadas} com {maior_peso} kg')
print(f'Menor peso registrado: {pessoas_mais_leves} com {menor_peso} kg')
