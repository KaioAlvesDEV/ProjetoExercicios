# BETA v1.1 - Boletim com Listas Compostas

sair = False
alunos_e_notas = [] # Lista para armazenar nomes dos alunos e suas notas

# Loop para adicionar alunos e suas notas
while not sair:

    nome_aluno = input('Digite o nome do aluno: ').title().strip()
    notas_aluno = [] # Lista para armazenar as duas notas do aluno

    # Coletar as duas notas do aluno
    for i in range(0, 2):

        notas_aluno.append(float(input(f'Digite a {i + 1}ª nota de {nome_aluno}: ')))
    
    while True:
        sair_input = input('Deseja sair? (S/N): ').upper().strip()
        if sair_input in ('S', 'N', 'SIM', 'NÃO'):
            break
        
    alunos_e_notas.append([nome_aluno, notas_aluno])
    
    if sair_input in ('S', 'SIM'):
        sair = True
        break

print(alunos_e_notas)
